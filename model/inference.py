import os

with open("serialized_bin", "rb") as f:
    import types

    serialized = marshal.loads(f.read())
    predict = types.FunctionType(serialized, globals(), "inference_wrapper")

def inference(reviews, val):
    forML = '<|prompter|>' + 'Given the reviews of this product give me its ' + val + ' in a list format only.' + ' ' + reviews[0] + ' ' + reviews[1] + ' ' + reviews[2] + ' ' + reviews[3] + '<|endoftext|><|assistant|>'
    return inference_wrapper(forML)
