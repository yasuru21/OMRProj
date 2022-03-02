
class sheetmusic:
    def getPitchDictionary(self, lines,dist): # dictionary used to calculate what note is which, IT IS IMPORTANT THAT STAVES ARE DETECTED CORRECTLY
            p = {}
            j = 1 # starts at stave #1 and iterates through each one checking if it is on line or not
            for i in lines:
                if j%2 ==0: # on line
                    p[int(i-dist*1.5)] = 'D'
                    p[int(i-dist)] = 'C'
                    p[int(i-dist*0.5)] = 'B'
                    p[i] = 'A'
                    p[int(i+dist*0.5)] = 'G'
                    p[int(i+dist)] = 'F'
                    p[int(i+dist*1.5)] = 'E'
                    p[int(i+dist*2)] = 'D'
                    p[int(i+dist*2.5)] = 'C'
                    p[int(i+dist*3)] = 'B'
                    p[int(i+dist*3.5)] = 'G'
                    p[int(i+dist*4)] = 'F'
                    p[int(i+dist*4.5)] = 'E'
                else: # not on line
                    p[int(i-dist*0.5)] = 'G'
                    p[i] = 'F'
                    p[int(i+dist*0.5)] = 'E'
                    p[int(i+dist)] = 'D'
                    p[int(i+dist*1.5)] = 'C'
                    p[int(i+dist*2)] = 'B'
                    p[int(i+dist*2.5)] = 'A'
                    p[int(i+dist*3)] = 'G'
                    p[int(i+dist*3.5)] = 'F'
                    p[int(i+dist*4)] = 'E'
                    p[int(i+dist*4.5)] = 'D'
                    p[int(i+dist*5)] = 'B'
                j += 1
            return p