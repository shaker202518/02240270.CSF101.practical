BinarySearch(ARR, X, LOW, HIGH)
       repeat till LOW = HIGH
              MID = (LOW + HIGH)/2
              if (X == ARR[mid])
                  return MID
              else if (x > ARR[MID]) 
                  LOW = MID + 1
              else                  
                  HIGH = MID – 1
