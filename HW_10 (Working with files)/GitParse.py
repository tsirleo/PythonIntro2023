import zlib
import sys

_object = sys.stdin.buffer.read()

if _object[:4] == b"PACK":   # https://git-scm.com/docs/pack-format
    print(f"pack: {int.from_bytes(_object[4:8])} {int.from_bytes(_object[8:12])}")
elif _object[0:4] == b"\377tOc":
    print(f"index: {int.from_bytes(_object[1028:1032])}")  # https://git-scm.com/docs/pack-format
else:
    try:
        data = zlib.decompress(_object)
        # print(data)
        header = data.split()[0]
        match header:
            case b"blob":
                stop_ind = data.find(b"\x00")
                print(f"blob: {data[len(header) + 1 : stop_ind].decode()}")
            case b"tree":
                start_ind = data.find(b"\x00")
                data = data[start_ind + 1:]
                print(f"tree: ")
                while data:
                    sep1 = data.find(b" ")
                    sep2 = data.find(b"\x00")
                    print(f"  {data[sep2 + 1: sep2 + 21].hex()} {data[:sep1].decode()} {data[sep1 + 1:sep2].decode()}")
                    data = data[sep2 + 21:]
            case b"tag":
                start_ind = data.find(b"\ntag")
                stop_ind = data.find(b"\ntagger")
                print(f"tag: {data[start_ind:stop_ind].split()[1].decode()}")
            case b"commit":
                start_ind = data.find(b"\x00tree")
                stop_ind = data.find(b"\n")
                print(f"commit: {data[start_ind:stop_ind].split()[1].decode()}")
            case default:
                print(data)
    except Exception:
        print("unknown:")
