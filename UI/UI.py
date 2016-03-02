#coding:utf-8

import wx

class UI(wx.Frame):
	def __init__(self, parent, ID, title):
		wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(800, 600))
#menubar
		menubar = wx.MenuBar()  
		file = wx.Menu()  
		edit = wx.Menu()  
		help = wx.Menu()  
		file.Append(101, '&打开', '打开图片')  
		file.Append(102, '&保存', '保存图片')  
		file.AppendSeparator()  
		quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')  
		quit.SetBitmap(wx.Image ('stock_exit.png',  wx.BITMAP_TYPE_PNG).ConvertToBitmap())  
		file.AppendItem(quit)  
		edit.Append(201, 'check item1', '', wx.ITEM_CHECK)  
		edit.Append(202, 'check item2', kind= wx.ITEM_CHECK)  
		submenu = wx.Menu()  
		submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)  
		submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)  
		submenu.Append(303, 'radio item3', kind= wx.ITEM_RADIO)  
		edit.AppendMenu(203, 'submenu', submenu)  
		menubar.Append(file, '&文件')  
		menubar.Append(edit, '&编辑')  
		menubar.Append(help, '&帮助')
		self.SetMenuBar(menubar)
		self.Center()  		
		wx.EVT_MENU(self, 105, self.OnQuit)
#toolbar
		vbox = wx.BoxSizer(wx.VERTICAL)
		toolbox = wx.BoxSizer(wx.HORIZONTAL)

		mainbox = wx.BoxSizer(wx.HORIZONTAL)
                toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)
                toolbar.AddSimpleTool(1, wx.Image('home.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'home', 'Home')
                toolbar.AddSimpleTool(2, wx.Image('mine.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'mine', 'Mine')
                toolbar.AddSeparator()
                toolbar.AddSimpleTool(3, wx.Image('exit.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'exit', 'Exit')
		toolbar.AddSeparator()
		toolbar.AddSimpleTool(4, wx.Image('search.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'search', 'Search')		
                toolbar.Realize()
                toolbox.Add( toolbar, 0, wx.EXPAND)
		
		searchbar = wx.Panel(self, -1)
		searchtext = wx.TextCtrl(searchbar, -1, '查找壁纸', pos = (20,5), size = (300, 40))
#		self.Bind(wx.EVT_BUTTON, self.OnSearch, searchbutton)
		searchtext.SetInsertionPoint(0)
		toolbox.Add(searchbar, 0, wx.EXPAND)
		#toolbox.Add(searchtext, 0, wx.EXPAND)		
		
		typebox = wx.BoxSizer(wx.VERTICAL)
		typebar = wx.ToolBar(self, -1, style = wx.TB_VERTICAL | wx.NO_BORDER)
		typebar.AddSimpleTool(11, wx.Image('11.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '风景', '风景')
		typebar.AddSimpleTool(12, wx.Image('12.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '动漫', '动漫')
		typebar.AddSimpleTool(13, wx.Image('13.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '萌宠', '萌宠')
		typebar.AddSimpleTool(14, wx.Image('14.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '汽车', '汽车')
		typebar.AddSimpleTool(15, wx.Image('15.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '游戏', '游戏')
		typebar.AddSimpleTool(16, wx.Image('16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), '影视', '影视')
		typebar.Realize()
		typebox.Add(typebar, 0, wx.EXPAND)

		picbox = wx.BoxSizer(wx.HORIZONTAL)
		picbox_left = wx.BoxSizer(wx.VERTICAL)
		picbox_right = wx.BoxSizer(wx.VERTICAL)
		pp11 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
		pp12 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)		
                pp13 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
                pp21 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
                pp22 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
                pp23 = wx.Panel(self, -1, style = wx.SIMPLE_BORDER)
		picbox_left.Add(pp11, 1, wx.EXPAND | wx.ALL, 3)
                picbox_left.Add(pp12, 1, wx.EXPAND | wx.ALL, 3)
                picbox_left.Add(pp13, 1, wx.EXPAND | wx.ALL, 3)
                picbox_right.Add(pp21, 1, wx.EXPAND | wx.ALL, 3)
                picbox_right.Add(pp22, 1, wx.EXPAND | wx.ALL, 3)
                picbox_right.Add(pp23, 1, wx.EXPAND | wx.ALL, 3)
		
		image = wx.Image("test.jpg",wx.BITMAP_TYPE_ANY)
		temp = image.ConvertToBitmap()
		
		wx.StaticBitmap(parent = pp11, bitmap = temp, size = (320,180))
		

		picbox.Add(picbox_left, 1, wx.EXPAND)
		picbox.Add(picbox_right, 1, wx.EXPAND)
		
		mainbox.Add(typebox, 0, wx.EXPAND)
		mainbox.Add(picbox, 0, wx.EXPAND)
		vbox.Add(toolbox, 0, wx.EXPAND)
		vbox.Add(mainbox, -1, wx.EXPAND)

                wx.EVT_TOOL(self, 1, self.OnHome)
                wx.EVT_TOOL(self, 2, self.OnMine)
                wx.EVT_TOOL(self, 3, self.OnQuit)
		wx.EVT_TOOL(self, 4, self.OnSearch)

		self.SetSizer(vbox)
		self.statusbar = self.CreateStatusBar()
		
		self.Centre()

#响应函数
	def OnHome(self, event):
		self.statusbar.SetStatusText('Home Command')
	def OnMine(self, event):
		self.statusbar.SetStatusText('Mine Command')
	def OnSearch(self, event):
		self.statusbar.SetStatusText('Search Command')
	def OnOpen(self, event):
		self.statusbar.SetStatusText('Open Command')
	def OnSave(self, event):
		self.statusbar.SetStatusText('Save Command')
	def OnQuit(self, event):
		self.Close()



class MyApp(wx.App):
	def OnInit(self):
		frame = UI(None, -1, '壁纸系统')
		frame.SetIcon(wx.Icon('logo.ico', wx.BITMAP_TYPE_ICO))
		frame.Center()
		frame.Show(True)
		return True
app = MyApp(0)
app.MainLoop()
