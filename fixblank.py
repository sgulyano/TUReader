import numpy as np

def fixblankname(df, cols):
    idxall = df[cols].isna().all(axis=1)
    idxany = df[cols].isna().any(axis=1)
    
    _, uidx, counts = np.unique((~idxall).cumsum(), return_inverse=True, return_counts=True)
    nanidx = np.where(counts > 1)[0]
    badidx = (uidx[:,np.newaxis] == nanidx).any(axis=1)
    return df[idxany | badidx]