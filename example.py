import wx
import pyHook

class myFrame(wx.Frame):
  def __init__(self):
    wx.Frame.__init__(self, None, -1, 'My Frame')

    # create the hook mananger
    self.hm = pyHook.HookManager()
    # register two callbacks
    self.hm.MouseAllButtonsDown = self.OnMouseEvent
    self.hm.KeyDown = self.OnKeyboardEvent

    # hook into the mouse and keyboard events
    self.hm.HookMouse()
    self.hm.HookKeyboard()

    wx.EVT_CLOSE(self, self.OnClose)

  def OnMouseEvent(self, event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'
    
    # return True to pass the event to other handlers
    # return False to stop the event from propagating
    return True

  def OnKeyboardEvent(self, event):
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Key:', event.Key
    print 'KeyID:', event.KeyID
    print 'ScanCode:', event.ScanCode
    print 'Extended:', event.Extended
    print 'Injected:', event.Injected
    print 'Alt', event.Alt
    print 'Transition', event.Transition
    print '---'
    
    # return True to pass the event to other handlers
    # return False to stop the event from propagating    
    return True

  def OnClose(self, event):
    del self.hm
    self.Destroy()

if __name__ == '__main__':
  app = wx.PySimpleApp(0)
  frame = myFrame()
  app.SetTopWindow(frame)
  frame.Show()
  app.MainLoop()