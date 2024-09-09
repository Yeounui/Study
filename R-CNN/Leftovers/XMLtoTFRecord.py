for IMGCount, prp_file in enumerate(prp_files):
    GroundTruthArray = tf.TensorArray(tf.int32, size=0, dynamic_size=True)

    filename = prp_file.split(".")[0]
    tree = ET.parse(open(os.path.join(path_list[0], path_list[1], filename + ".xml"), "r"))
    root = tree.getroot()

    for i, _obj in enumerate(root.findall("object")):
        bndbox = _obj.find("bndbox")
        GroundTruthArray.write(i, tf.constant([int(bndbox.find("ymin").text), int(bndbox.find("xmin").text),
                                               int(bndbox.find("ymax").text),
                                               int(bndbox.find("xmax").text)])).mark_used()