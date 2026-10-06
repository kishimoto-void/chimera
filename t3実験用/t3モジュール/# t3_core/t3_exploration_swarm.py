# T3 Exploration Swarm / Direction Formation Experiment
from dataclasses import dataclass
from typing import List, Optional, Sequence
import math

def sign(x, eps=1e-12):
    return 1 if x > eps else (-1 if x < -eps else 0)

@dataclass
class ExplorationPoint:
    step:int; state:float; residual:float; direction:int; magnitude:float

@dataclass
class SwarmWindow:
    start:int; end:int; count:int
    swarm_score:float; direction_bias:float; vector_candidate:float
    reversal_rate:float; directional_entropy:float
    magnitude_mean:float; magnitude_std:float
    previous_vector:Optional[float]=None; vector_delta:Optional[float]=None

@dataclass
class FormationResult:
    points:List[ExplorationPoint]; windows:List[SwarmWindow]
    peak_swarm_window:Optional[int]
    first_direction_window:Optional[int]
    first_strong_direction_window:Optional[int]
    notes:List[str]

class ExplorationSwarmAnalyzer:
    """Observe residual swarm and directional formation; no physical force is assumed."""
    def __init__(self, window_size=5, strong_direction_threshold=.60, eps=1e-12):
        if window_size < 2: raise ValueError("window_size must be >= 2")
        self.window_size=window_size; self.strong_direction_threshold=strong_direction_threshold; self.eps=eps

    def make_points(self, states:Sequence[float]):
        return [ExplorationPoint(i,float(states[i]),float(states[i+1])-float(states[i]),sign(float(states[i+1])-float(states[i])),abs(float(states[i+1])-float(states[i]))) for i in range(max(0,len(states)-1))]

    def analyze(self, states, window_size=None):
        points=self.make_points(states)
        if not points: return FormationResult([],[],None,None,None,["INSUFFICIENT_STATES"])
        ws=window_size or self.window_size
        windows=[]
        for start in range(0,len(points),ws):
            c=points[start:start+ws]
            if len(c)<2: break
            vals=[p.residual for p in c]; mags=[p.magnitude for p in c]; dirs=[p.direction for p in c]
            vector=self._weighted_direction(vals); bias=self._direction_bias(vals); rev=self._reversal_rate(dirs); ent=self._entropy(dirs)
            mm=self._mean(mags); sd=self._std(mags); disp=sd/(mm+self.eps) if mm>self.eps else 0.0
            swarm=self._clamp01(.45*self._clamp01(disp)+.30*ent+.25*rev)
            windows.append(SwarmWindow(c[0].step,c[-1].step,len(c),swarm,bias,vector,rev,ent,mm,sd))
        for i in range(1,len(windows)):
            windows[i].previous_vector=windows[i-1].vector_candidate
            windows[i].vector_delta=windows[i].vector_candidate-windows[i-1].vector_candidate
        peak=max(range(len(windows)),key=lambda i:windows[i].swarm_score) if windows else None
        first=next((i for i,w in enumerate(windows) if abs(w.vector_candidate)>self.eps),None)
        strong=next((i for i,w in enumerate(windows) if abs(w.vector_candidate)>=self.strong_direction_threshold),None)
        notes=[]
        if peak is not None: notes.append(f"PEAK_SWARM_WINDOW={peak}")
        if first is not None: notes.append(f"FIRST_DIRECTION_WINDOW={first}")
        if strong is not None: notes.append(f"FIRST_STRONG_DIRECTION_WINDOW={strong}")
        if peak is not None and strong is not None:
            notes.append("DIRECTION_AFTER_SWARM_PEAK_CANDIDATE" if strong>peak else "DIRECTION_PRECEDES_SWARM_PEAK" if strong<peak else "DIRECTION_AND_SWARM_PEAK_SAME_WINDOW")
        if all(abs(w.vector_candidate)<=self.eps for w in windows): notes.append("NO_DIRECTIONAL_BIAS")
        if all(w.reversal_rate==0 for w in windows): notes.append("NO_REVERSAL")
        return FormationResult(points,windows,peak,first,strong,notes)

    def _weighted_direction(self, rs):
        total=sum(abs(r) for r in rs); return sum(rs)/total if total>self.eps else 0.0
    def _direction_bias(self, rs):
        p=sum(abs(r) for r in rs if r>self.eps); n=sum(abs(r) for r in rs if r< -self.eps); t=p+n
        return (p-n)/t if t>self.eps else 0.0
    def _reversal_rate(self, ds):
        ds=[d for d in ds if d]
        return sum(a!=b for a,b in zip(ds,ds[1:]))/(len(ds)-1) if len(ds)>=2 else 0.0
    def _entropy(self, ds):
        ds=[d for d in ds if d]
        if not ds:return 0.0
        p=sum(d==1 for d in ds)/len(ds); q=1-p
        return (-p*math.log2(p) if p else 0)+(-q*math.log2(q) if q else 0)
    @staticmethod
    def _mean(x): return sum(x)/len(x) if x else 0.0
    @staticmethod
    def _std(x):
        if not x:return 0.0
        m=sum(x)/len(x); return math.sqrt(sum((v-m)**2 for v in x)/len(x))
    @staticmethod
    def _clamp01(x): return max(0.0,min(1.0,x))

def print_result(r):
    print("WINDOWS")
    for i,w in enumerate(r.windows):
        print(f"W{i}: swarm={w.swarm_score:.3f} bias={w.direction_bias:+.3f} vector={w.vector_candidate:+.3f} rev={w.reversal_rate:.3f} entropy={w.directional_entropy:.3f} |r|mean={w.magnitude_mean:.2f}")
    print("NOTES", r.notes)

def demo():
    a=ExplorationSwarmAnalyzer(5,.60)
    cases={
      "A_swarm_then_direction":[0,8,3,11,4,5,7,10,14,19,25,32,40,49,59],
      "B_direction_first":[0,2,5,9,14,20,27,35,44,54,65,77,90,104,119],
      "C_persistent_oscillation":[0,10,2,12,3,13,4,14,5,15,6,16,7,17,8,18,9]
    }
    for name,states in cases.items():
        print("\nCASE",name); print_result(a.analyze(states))
if __name__=='__main__': demo()
