import instaloader
import pandas as pd
import os
import json
import time
import random

# 參數設定
USERNAME = "david_chung_04"
TARGET_USERNAME = "nulniix"
LIMIT_POSTS = 428

# 初始化 Instaloader
L = instaloader.Instaloader()

# 讀取 Session
session_file = r"C:\Users\workh\AppData\Local\Instaloader\session-david_chung_04"
L.load_session_from_file(USERNAME, filename=session_file)
print("成功讀取 Session！")

# 讀取目標帳號
profile = instaloader.Profile.from_username(L.context, TARGET_USERNAME)

# 開始擷取
post_data = []
counter = 0

posts = profile.get_posts()

while counter < LIMIT_POSTS:
    try:
        post = next(posts)
        post_data.append({
            "編號": counter + 1,
            "發文日期": post.date.strftime('%Y-%m-%d %H:%M:%S'),
            "發文文字": post.caption,
            "按讚數": post.likes,
            "留言數": post.comments
        })

        counter += 1
        print(f"已擷取第 {counter} 篇")

        # 每篇 sleep 1~3 秒 (隨機)
        time.sleep(random.uniform(1, 3))

        # 每抓滿 20篇，主動 sleep 30秒降風控
        if counter % 20 == 0:
            print("稍作休息，模擬人類滑動習慣...")
            time.sleep(30)

    except instaloader.exceptions.QueryReturnedBadRequestException as e:
        print(f"遭遇 IG 風控，暫停 5分鐘再繼續：{e}")
        time.sleep(300)
    except Exception as e:
        print(f"擷取第 {counter+1} 篇時發生未知錯誤：{e}")
        time.sleep(5)

# 存成 Excel
df = pd.DataFrame(post_data)
df.to_excel(f"{TARGET_USERNAME}_IG_Posts.xlsx", index=False, engine='openpyxl')
print(f"成功擷取 {counter} 篇貼文，結果已匯出為 Excel！")

# 存成 JSON
json_filename = f"{TARGET_USERNAME}_IG_Posts.json"
with open(json_filename, "w", encoding="utf-8") as f:
    json.dump(post_data, f, ensure_ascii=False, indent=4)

print(f"成功匯出 JSON 檔案：{json_filename}")
