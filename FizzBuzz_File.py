def FizzBuzz(start, finish):
    numvec = np.arange(start, finish + 1)
    objvec = np.array(numvec, dtype=object)
    
    fizz_mask = (numvec % 3 == 0)
    buzz_mask = (numvec % 5 == 0)
    
    objvec[fizz_mask & buzz_mask] = 'fizzbuzz'
    objvec[fizz_mask & ~buzz_mask] = 'fizz'
    objvec[~fizz_mask & buzz_mask] = 'buzz'
    
    return objvec
