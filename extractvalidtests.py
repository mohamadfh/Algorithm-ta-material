
from bs4 import BeautifulSoup
import os


def extract_valid_inputs(address):
    with open(address, 'r',encoding="utf8") as f:

        contents = f.read()

        soup = BeautifulSoup(contents)
        inputs = soup.find_all("pre", {"class": "input"})
        outputs = soup.find_all("pre", {"class": "answer"})

        valid_inputs = list()
        valid_outputs = list()

        for testcase in range(len(inputs)):
            if(not inputs[testcase].text.endswith("...") and not outputs[testcase].text.endswith("...")):
                valid_inputs.append(inputs[testcase].text)
                valid_outputs.append(outputs[testcase].text)
            else:
                print(testcase)

    return valid_inputs ,valid_outputs

def save_tests(inputs,outputs):
    try:
        os.mkdir("./out")
    except:
        pass
    os.chdir("./out")
    for out in range(len(outputs)):
        with open(f'output{out}.txt', 'w') as writer:
            writer.write(outputs[out])
    try:
        os.mkdir("../in")
    except:
        pass
    os.chdir("../in")
    for inp in range(len(inputs)):
        with open(f'input{inp}.txt', 'w') as writer:
            writer.write(inputs[inp])
if __name__ == "__main__":
    ins, outs = extract_valid_inputs("sb.html")
    save_tests(ins,outs)
