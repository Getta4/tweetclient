###インポート###
import tweepy
import tkinter as tk
from tkinter import messagebox
import webbrowser

###認証情報の読み込み###
try:
    with open("userkey.txt", "r",encoding="utf-8_sig") as f:
        lines = f.readlines()
        try:
            apikey = lines[0].strip()
            apiSecret = lines[1].strip()
            accessToken = lines[2].strip()
            accessSecret = lines[3].strip()
        except:
            apikey = ""
            apiSecret = ""
            accessToken = ""
            accessSecret = ""
    lines_rstrip = [line.rstrip("\n") for line in lines]
    #print(lines_rstrip)
except:
    with open("userkey.txt", "w",encoding="utf-8_sig") as f:
        try:
            apikey = lines[0].strip()
            apiSecret = lines[1].strip()
            accessToken = lines[2].strip()
            accessSecret = lines[3].strip()
        except:
            apikey = ""
            apiSecret = ""
            accessToken = ""
            accessSecret = ""
    lines_rstrip = [line.rstrip("\n") for line in lines]
    #print(lines_rstrip)
    

###変数の設定###
window = tk.Tk()
posX = tk.X
posY = tk.Y
setFile = False
filename = None

#テキストの内容から認証情報を取得、内容がない場合にはインフォメーションを表示
for line in lines_rstrip:
    if line == 0:
        apikey = lines_rstrip[line]
    if line == 1:
        apiSecret = lines_rstrip[line]
    if line == 2:
        accessToken = lines_rstrip[line]
    if line == 3:
        accessSecret = lines_rstrip[line]

#print (apikey, apiSecret, accessToken, accessSecret)

auth = None
api = None
client = None

###関数の設定###

def tweet():
    #グローバル化
    global api
    global client
    global auth
    global setFile
    #入力情報を取得
    tweet = text.get("1.0", tk.END)
    #print(tweet)
    if tweet == "\n":#未入力の場合は弾く
        messagebox.showerror("Error", "ツイート内容が入力されていません\n一文字以上内容を入力してください。")
        return
    #print(tweet)
    try:
        #認証
        auth = tweepy.OAuthHandler(apikey, apiSecret)
        auth.set_access_token(accessToken, accessSecret)

        #オブジェクト作成
        api = tweepy.API(auth)
        client = tweepy.Client(
            consumer_key = apikey,
            consumer_secret = apiSecret,
            access_token = accessToken,
            access_token_secret = accessSecret
        )
        if setFile == True:#画像ファイルがあるときの処理
            image_path = filename
            media = api.media_upload(filename=image_path)
            client.create_tweet(text=tweet, media_ids=[media.media_id])
            setFile = False
            messagebox.showinfo("Success!", "ツイートが完了しました")
        else:
            client.create_tweet(text=tweet)
            setFile = False
            messagebox.showinfo("Success!", "ツイートが完了しました")
        #print(True)
    except:
        messagebox.showerror("Error", "認証情報が正しくありません\n設定から再度認証情報を入力してください。")
        #print(False)
        return

def close_window(root, apikey2, apiSecret2, accessToken2, accessSecret2):
    global apikey
    global apiSecret
    global accessToken
    global accessSecret

    apikey = apikey2.get()
    apiSecret = apiSecret2.get()
    accessToken = accessToken2.get()
    accessSecret = accessSecret2.get()
    
    root.destroy()

    #入力内容を保存
    file = open(".secret/userkey.txt", "w")
    file.write(apikey + "\n" + apiSecret + "\n" + accessToken + "\n" + accessSecret)
    file.close()

def setting():
    root = tk.Tk()

    root.title("ログイン情報の入力")
    root.geometry("400x120")

    apikey_label = tk.Label(root,text="API Key")
    apikey_label.grid(row=1, column=1, padx=10)

    apikey = tk.Entry(root,show="*",width=48)
    apikey.grid(row=1, column=2)

    apiSecret_label = tk.Label(root,text="API Secret")
    apiSecret_label.grid(row=2, column=1, padx=10)

    apiSecret = tk.Entry(root,show="*", width=48)
    apiSecret.grid(row=2, column=2)

    accessToken_label = tk.Label(root,text="Client ID")
    accessToken_label.grid(row=3, column=1, padx=10)

    accessToken = tk.Entry(root,show="*",width=48)
    accessToken.grid(row=3, column=2)

    accessSecret_label = tk.Label(root,text="Client Secret")
    accessSecret_label.grid(row=4, column=1, padx=10)

    accessSecret = tk.Entry(root,show="*", width=48)
    accessSecret.grid(row=4, column=2)


    button = tk.Button(root,text="Submit", command=lambda: close_window(root, apikey, apiSecret, accessToken, accessSecret))
    button.place(x=180, y=90)

    root.mainloop()

def openGithub():
    webbrowser.open("https://github.com/getta4/TweetClient",new=1,autoraise=True)

def openFileDialog():
    global filename
    global setFile
    import tkinter.filedialog
    filename = tkinter.filedialog.askopenfilename(title="画像ファイルを選択してください",filetypes=[("画像ファイル","*.png *.jpg *.jpeg *.gif")])
    setFile = True
    #print(filename)

###Windowの基本設定###
window.title("Tweet Client")
window.geometry("700x400")
window.resizable(False, False)
window.minsize(700, 400)

cv = tk.Canvas(window, width=700, height=400,bg="black") #キャンバスを作成
cv.pack(expand=True, fill=tk.BOTH)

###要素の配置###
info_label = tk.Label(cv, text="ツイートの内容を入力してください", bg="black", fg="white",height=10, font=("Arial", 16))
info_label.place(x=5, y=5, relheight=0.1)
text = tk.Text(cv,height=10,width=50,font=("Arial", 14))
text.place(x=10,y=40,relwidth=0.9,relheight=0.4)#,expand=True)
submit_button = tk.Button(cv,text="ツイート", font=("Arial", 14),command=tweet)
submit_button.place(x=10,y=210,relwidth=0.2, relheight=0.1)
submit_button = tk.Button(cv,text="画像を選択", font=("Arial", 14),command=openFileDialog)
submit_button.place(x=160,y=210,relwidth=0.2, relheight=0.1)

other_label = tk.Label(cv, text="その他", bg="black", fg="white",height=10, font=("Arial", 16))
other_label.place(x=5, y=300, relheight=0.1)
settings_button = tk.Button(cv,text="設定", font=("Arial", 14),command=setting)
settings_button.place(x=10,y=340,relwidth=0.2, relheight=0.1)
settings_button = tk.Button(cv,text="Github", font=("Arial", 14),command=openGithub)
settings_button.place(x=160,y=340,relwidth=0.2, relheight=0.1)

###メインループ###
if apikey == "" or apiSecret == "" or accessToken == "" or accessSecret == "":
    messagebox.showinfo("Info", "認証情報が入力されていません\n設定から認証情報を入力してください。")
    setting()
window.mainloop()