# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py',
r'F:\python项目\XueXiTongAutoFlush\package\display.py',
r'F:\python项目\XueXiTongAutoFlush\package\exception.py',
r'F:\python项目\XueXiTongAutoFlush\package\internetTime.py',
r'F:\python项目\XueXiTongAutoFlush\package\dataManger.py',
r'F:\python项目\XueXiTongAutoFlush\package\progressbar.py',
r'F:\python项目\XueXiTongAutoFlush\package\user.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\xueXiTong.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\learnable.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\school.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\audio.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\exam.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\PPT.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\video.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\taskInterface.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\answerQuestion\answerable.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\answerQuestion\getAnswer.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\answerQuestion\homework.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\answerQuestion\multipleChoiceOfTask.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\answerQuestion\question.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\task\answerQuestion\trueOrFalseOfTask.py',
r'F:\python项目\XueXiTongAutoFlush\package\ControlWeb\Spider\spider.py'],
             pathex=[r'F:\python项目\XueXiTongAutoFlush'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='刷课程序3.2.1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          icon='.\学习.ico')
