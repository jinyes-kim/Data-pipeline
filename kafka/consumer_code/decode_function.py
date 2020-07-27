def decoding(bytes_data):
    return bytes_data.decode('utf-8')


def msg_decode(msg):
    data = msg.value
    data = data.split()
    res = list(map(decoding, data))
    return res
