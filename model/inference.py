import os
import marshal

with open("serialized_bin", "rb") as f:
    import types

    serialized = marshal.loads(f.read())
    predict = types.FunctionType(serialized, globals(), "inference_wrapper")

def inference(reviews, val):
    forML = '<|prompter|>' + 'Given the reviews of this product give me its ' + val + ' in a list format only.' + ' ' + reviews[0] + ' ' + reviews[1] + ' ' + reviews[2] + ' ' + reviews[3] + '<|endoftext|><|assistant|>'
    out = predict(forML)
    out = out[0]['generated_text'].split('\n')
    out.pop(0)
    for i in range(len(out)):
        out[i] = out[i][2:]
    points = ''
    for j in out:
        points += j + '.' + ' '

    return points

# print(inference('<|prompter|>Given the reviews of this product give me its cons in a list format only. This turned out amazing! So cute and such good quality. The shop owner even took the liberty of putting photos together with the same color scheme/tones for a more cohesive layout. Just perfect! The book arrived very quickly, considering it’s all custom made! It is very small, which maybe I just didn’t notice in the photos. But I was mostly bummed by the cropping/arrangement of the book. It would have been really nice if a preview was sent first? I was hoping all my photos would be placed vertically and cropped appropriately, but it was organized and laid out according to what the seller thought I wanted without any consultation. And some had to have the blurred edges just to fit in that orientation. It’s definitely a cool concept, but it just didn’t compare to the photos I saw in the post The photos are so high quality. I’m not sure what I was expecting when I ordered but it went above my expectations. Shipping is also fast and I can’t wait to give the little book as a present. I will be ordering from them again The magnet that holds the book closed is really not great quality. Other than that I am very pleased and I absolutely love my keychain!<|endoftext|><|assistant|>'))