from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

from time import strftime


class ClockApp(App):
    sw_started = False
    sw_seconds = 0

    def update_time(self, nap):
        self.root.ids.time.text = strftime('[b]%H[/b]:%M:%S')
        if self.sw_started :
            self.sw_seconds += nap
        minutes, seconds = divmod(self.sw_seconds, 60)
        self.root.ids.stopwatch.text = (
            '%02d:%02d.[size=40]%02d[/size]' %
            (int(minutes), int(seconds),
            int(seconds * 100 % 100)))

    #很多程序监听共同事件之一就是App.on_start，定义在类里面，在app初始化的时候调用。
    #另一个常见的是on_press，当用户点击，tap，或其他按钮操作时启用。    
    def on_start(self):
        Clock.schedule_interval(self.update_time, 0)

    def start_stop(self):
        self.root.ids.start_stop.text = ('Start'
            if self.sw_started else 'Stop')
        self.sw_started = not self.sw_started

    def reset(self):
        if self.sw_started:
            self.root.ids.start_stop.text = 'Start'
            self.sw_started = False
        self.sw_seconds = 0


if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#2f62c6') #调整窗口背景色
    ClockApp().run()