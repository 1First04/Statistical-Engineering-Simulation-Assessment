# __int__ difinition 

def __init__(self, data: List[Union[Number, str, None]]):
        self.raw_data = data
        self.data = self._clean_data(data)
  
  def __init__(self, crash_prob=0.045, seed=42):
        self.crash_prob = crash_prob
        random.seed(seed)
