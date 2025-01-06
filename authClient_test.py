import tkinter as tk

root = tk.Tk()

root.title("ログイン情報の入力")
root.geometry("400x120")

apikey_label = tk.Label(text="API Key")
apikey_label.grid(row=1, column=1, padx=10)

apikey = tk.Entry(show="*",width=48)
apikey.grid(row=1, column=2)

apiSecret_label = tk.Label(text="API Secret")
apiSecret_label.grid(row=2, column=1, padx=10)

apiSecret = tk.Entry(show="*", width=48)
apiSecret.grid(row=2, column=2)

clientID_label = tk.Label(text="Client ID")
clientID_label.grid(row=3, column=1, padx=10)

clientID = tk.Entry(show="*",width=48)
clientID.grid(row=3, column=2)

clientSecret_label = tk.Label(text="Client Secret")
clientSecret_label.grid(row=4, column=1, padx=10)

clientSecret = tk.Entry(show="*", width=48)
clientSecret.grid(row=4, column=2)


button = tk.Button(text="Submit", command=lambda: close_window(root, apikey, apiSecret, clientID, clientSecret))
button.place(x=180, y=90)

def close_window(root, apikey2, apiSecret2, clientID2, clientSecret2):
    global apikey
    global apiSecret
    global clientID
    global clientSecret
    apikey = apikey2.get()
    apiSecret = apiSecret2.get()
    clientID = clientID2.get()
    clientSecret = clientSecret2.get()
    root.destroy()

root.mainloop()

print(apikey)
print(apiSecret)
print(clientID)
print(clientSecret)
