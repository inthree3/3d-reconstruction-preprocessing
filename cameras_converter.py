def read_cam_txt(cam_txt_path):
    if not os.path.exists(cam_txt_path):
        raise Exception(f"No such file : {cam_txt_path}")

    with open(cam_txt_path, 'r') as f:
        lines = f.readlines()

    if len(lines) < 3:
        raise Exception(f"Invalid cameras.txt file : {cam_txt_path}")

    comments = lines[:3]
    contents = lines[3:]

    ids = []
    Ks = []
    dists = []
    img_dims = [] # (w, h)


    for cam_idx, content in enumerate(contents):
        content_items = content.split(' ')
        cam_id = content_items[0]
        cam_type = content_items[1]
        img_w, img_h = int(content_items[2]), int(content_items[3])

        if cam_type == "OPENCV":
            fx, fy = content_items[4], content_items[5]
            cx, cy = content_items[6], content_items[7]
            K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=np.float32)
            dist = content_items[8:] + [0] # k1 k2 p1 p2 + k3(0)
            dist = np.asarray(dist)
            ids.append(cam_id)
            Ks.append(K)
            dists.append(dist)
            img_dims.append((img_w, img_h))
        elif cam_type== "PINHOLE":
            fx, fy = content_items[4], content_items[5]
            cx, cy = content_items[6], content_items[7]
            K = np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]], dtype=np.float32)
            dist = np.zeros([5], dtype=np.float32)
            ids.append(cam_id)
            Ks.append(K)
            dists.append(dist)
            img_dims.append((img_w, img_h))
        else:
            raise NotImplementedError(f"Only opencv/pinhole camera will be supported.")

    return ids, Ks, dists, img_dims