def detectByPathVideo(path, writer):
            while video.isOpened():
                if check == True:
                    count = 0
                    for i in range(len(boxes)):
                        if classes[i] == 1 and scores[i] > threshold:
                            count += 1
                            cv2.putText(img, f'Total Persons: {count}', (20, 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,0), 2)
                global filename2, max_count2, framex2, county2, max2, avg_acc2_list, max_avg_acc2_list, max_acc2, max_avg_acc2
                max_count2 = 0
                framex2 = []
                county2 = []
                max2 = []
                avg_acc2_list = []
                max_avg_acc2_list = []
                max_acc2 = 0
                max_avg_acc2 = 0