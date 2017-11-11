import multi_get

if __name__ == "__main__":
    ids = ["89575","233835","192416"]
    data = multi_get.multi_get(ids)
    print(data.text)
