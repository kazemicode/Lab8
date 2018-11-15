## Sara Kazemi
## Lab 8

def main():
  s = getSnd()
  samples = getSamples(s)
  print
  print "original"
  print "------"
  print samples[10730]
  print samples[20350]
  print
  increaseVolume(s)
  print "after increase"
  print "--------------"
  print samples[10730]
  print samples[20350]
  print
  decreaseVolume(s)
  print "after decrease"
  print "-------------"
  print samples[10730]
  print samples[20350]
  changeVolume(s,0.5)
  print
  print "CHANGE VOLUME"
  print "---------------"
  print samples[10730]
  print samples[20350]
  maxVolume(s)
  print
  print "MAX VOLUME"
  print "---------------"
  print samples[10730]
  print samples[20350]
  goToEleven(s)
  print
  print "GO TO ELEVEN"
  print "---------------"
  print samples[10730]
  print samples[20350]

def getSnd():
  return makeSound(pickAFile())

def increaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 2)
   return sound
   
def decreaseVolume(sound):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * 0.5)
   return sound
      
def changeVolume(sound,n):
   for sample in getSamples(sound):
      value = getSampleValue(sample)
      setSampleValue(sample, value * n)
   return sound

# maxSample: Finds a multiplier that will give us the loudest volume 
# that we can get based on a maximum sound sample and then boosts 
# the sound values by that amount. 
def maxSample(sound):
  largest = 0
  for sample in getSamples(sound):
    largest = max(largest,getSampleValue(sample))
  return largest

# maxVolume: increases the volume of each sample by the factor 
# (factor=float(maxPossibleSampleValue)/largest)
# where largest is the value returned by your maxSample function.
def maxVolume(sound):
  largest = maxSample(sound)
  factor = float(32767)/largest
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSample(sample, value * factor) 
  return sound

# goToEleven: Makes each sample the max or min
def goToEleven(sound):
  for sample in getSamples(sound):
    # For each sample, if the sample value is greater than 0, 
    # set the sample value to max
    if getSampleValue(sample) > 0:
      setSampleValue(sample, 32767)
    # If the sample value is less than 0, 
    #iSet the sample value to the minimum possible value: -32768.
    elif getSampleValue(sample) < 0:
      setSampleValue(sample, -32768)
  return sound
    
