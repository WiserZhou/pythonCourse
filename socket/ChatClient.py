import threading
from tkinter import *
from UdpClient import UdpClient
from queue import Queue


class ChatClient:
    def __init__(self, master, client):
        self.client = client
        self.master = master
        self.master.title('UDP Chat Client')
        self.master.geometry('600x400')

        self.frm = Frame(self.master)
        self.frm.pack()

        self.t_show = Text(self.frm, width=80, height=20, font=('Verdana', 10))
        self.t_show.pack()

        self.smsg = StringVar()

        self.entry_msg = Entry(self.frm, textvariable=self.smsg, width=50, font=('Fangsong', 12))
        self.entry_msg.pack(side=LEFT)
        self.btn_send = Button(self.frm, text="Send", command=self.send_message, width=8, height=1)
        self.btn_send.pack(side=LEFT)

        self.msg_queue = Queue()
        self.master.after(100, self.process_queue)

        self.thread_stop = False

        # Start a new thread for receiving messages
        self.receiver_thread = threading.Thread(target=self.receive_messages)
        self.receiver_thread.start()

    def send_message(self):
        message = self.smsg.get()
        self.client.send_message(message)
        self.t_show.insert('end', 'Client: ' + message + '\n')
        self.t_show.see('end')
        self.smsg.set('')

    def receive_messages(self):
        while not self.thread_stop:
            data, addr = self.client.receive_message()
            if data:
                self.msg_queue.put(f'{addr}: {data}\n')

    def process_queue(self):
        while not self.msg_queue.empty():
            msg = self.msg_queue.get()
            self.t_show.insert('end', msg)
            self.t_show.see('end')
        self.master.after(100, self.process_queue)

    def close(self):
        self.thread_stop = True
        self.client.close()
        self.receiver_thread.join()
        self.master.destroy()


def main():
    root = Tk()
    client = UdpClient('127.0.0.1', 5004)
    app = ChatClient(root, client)
    root.protocol("WM_DELETE_WINDOW", app.close)
    root.mainloop()


if __name__ == '__main__':
    main()
