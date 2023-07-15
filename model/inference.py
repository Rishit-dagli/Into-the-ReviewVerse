with open("serialized_bin", "rb") as f:
    import types

    serialized = marshal.loads(f.read())
    predict = types.FunctionType(serialized, globals(), "inference_wrapper")
print(inference_wrapper("What is the Universe"))