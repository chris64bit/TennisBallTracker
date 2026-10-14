from scenedetect import open_video, SceneManager, ContentDetector

def scene_detect(path_video):
    """
    Split video to disjoint fragments based on color histograms
    """
    # 1. Buka video secara langsung (jangan gunakan list [] untuk path_video)
    video_manager = open_video(path_video)

    # 2. Siapkan scene manager dan detector
    scene_manager = SceneManager()
    scene_manager.add_detector(ContentDetector())

    # 3. Proses deteksi scene
    scene_manager.detect_scenes(video_manager)
    scene_list = scene_manager.get_scene_list()

    # 4. Ambil frame awal dan akhir
    if not scene_list:
        # Jika tidak ada potongan scene terdeteksi (video dianggap 1 scene utuh),
        # kembalikan nilai dari frame 0 hingga total frame video tersebut.
        # Menggunakan .duration.frame_num sebagai pengganti get_current_timecode()
        scenes = [[0, video_manager.duration.frame_num]]
    else:
        scenes = [[x[0].frame_num, x[1].frame_num] for x in scene_list]
        
    return scenes