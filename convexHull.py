# Reads an .obj file and returns/plots the perimeter points


def Left_index(points):
  
  '''
  Finding the left most point
  '''
  minn = 0
  for i in range(1,len(points)):
    if points[i][0] < points[minn][0]:
      minn = i
    elif points[i][0] == points[minn][0]:
      if points[i][1] > points[minn][1]:
        minn = i
  return minn

def orientation(p, q, r):
  '''
  To find orientation of ordered triplet (p, q, r).
  The function returns following values
  0 --> p, q and r are collinear
  1 --> Clockwise
  2 --> Counterclockwise
  '''
  val = (q[1] - p[1]) * (r[0] - q[0]) - \
    (q[0] - p[0]) * (r[1] - q[1])

  if val == 0:
    return 0
  elif val > 0:
    return 1
  else:
    return 2

def convexHull(points, n):
  result = open("objResult.txt", "w+")

  # There must be at least 3 points
  if n<3:
    return
  l = Left_index(points)
  hull = []
  
  '''
  Start from leftmost point, keep moving counterclockwise
  until reach the start point again. This loop runs O(h)
  times where h is number of points in result or output.
  '''
  p = l
  q = 0

  hullPoints = []

  while(True):
    
    # Add current point to result
    hull.append(p)

    '''
    Search for a point 'q' such that orientation(p, q,
    x) is counterclockwise for all points 'x'. The idea
    is to keep track of last visited most counterclock-
    wise point in q. If any point 'i' is more counterclock-
    wise than q, then update q.
    '''
    q = (p + 1) % n

    for i in range(n):
      
      # If i is more counterclockwise
      # than current q, then update q
      if(orientation(points[p],
            points[i], points[q]) == 2):
        q = i

    '''
    Now q is the most counterclockwise with respect to p
    Set p as q for next iteration, so that q is added to
    result 'hull'
    '''
    p = q

    # While we don't come to first point
    if(p == l):
      break

    # Print Result
    for each in hull:
      hullPoints.append([points[each][0], points[each][1]])

  result.close()
  return hullPoints

import sys

file = open(sys.argv[1], "r")
readStop = False

# result = open("objResult.txt", "w+")

nodes = []
for line in file:
  initialReadStop = readStop

  args = line.split()
  if (len(args) != 4):
    continue
  v = args[0]
  xPos = args[1]
  yPos = args[2]

  if (v == "v"):
    nodes.append([float(xPos), float(yPos)])
    # result.write("x: " + str(xPos) + ", y: " + str(yPos) + "\n")
  else:
    readStop = False

  if initialReadStop and not readStop:
    break

# result.close()
file.close()

import time

start = time.time()

hull = convexHull(nodes, len(nodes))
# sort, first by x, then by y
sortedHull = sorted(hull, key=lambda k: [k[0], k[1]])
end = time.time()
print(end - start)

import math
bestHull = []
d = 0.5

for index, p in enumerate(sortedHull):
  if index == 0:
    bestHull.append(p)
    lastBestHull = p
    continue

  distance = math.dist(lastBestHull, p)
  if distance >= d:
    bestHull.append(p)
    lastBestHull = p

print(len(bestHull))


##################### Show Plot #####################

import matplotlib as mpl
import matplotlib.pyplot as plt

x_values = [h[0] for h in hull]
y_values = [h[1] for h in hull]
plt.plot(x_values, y_values, "bo")

xb_values = [h[0] for h in bestHull]
yb_values = [h[1] for h in bestHull]
plt.plot(xb_values, yb_values, "ro")

plt.show()


