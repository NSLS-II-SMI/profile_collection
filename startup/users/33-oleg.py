####line scan

def scan_sample( det, motor, start, end, point  ):
    '''absolute scan
    For example,
        det =  [pil300KW, pil1M, pil1mroi2,pil1mroi3, ssacurrent]
        motor = sample.x
        start: -.1
        end: 1
        points: 10
    '''
    RE(bp.scan([det], motor, start, end, point ))
