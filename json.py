import json


def main():
    data = {}
    data["name"] = "Taro"
    data["age"] = "25"

    # print("{}".format(json.dumps(data,indent=4)))

    # write file
    fw = open('data.json', 'w')
    json.dump(data, fw, indent=4)


if __name__ == '__main__':
    main()
