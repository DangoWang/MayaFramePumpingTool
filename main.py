# -*- coding: utf-8 -*-

# author: wangdonghao
import ui
try:
    from PySide2 import QtWidgets, QtCore
    from shiboken2 import wrapInstance
except ImportError:
    import PySide.QtGui as QtWidgets
    from PySide import QtCore
    from shiboken import wrapInstance
    import pysideuic as uic

import maya.OpenMayaUI as mui
import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel


def get_maya_window():
    main_window_ptr = mui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)


class CutAnimFrames(ui.Ui_Dialog, QtWidgets.QDialog):
    def __init__(self, parent=get_maya_window()):
        super(CutAnimFrames, self).__init__(parent)
        self.setupUi(self)
        self.root_ctrl_pb.clicked.connect(self.input_root)
        self.track_ctrl_pb.clicked.connect(lambda : self.track_ctrl_le.setText(cmds.ls(sl=1)[0]))
        self.bake_pb.clicked.connect(self.bake_doit)

        self.locator = ''
        self.min_frame = int(cmds.playbackOptions(q=1, min=1))
        self.max_frame = int(cmds.playbackOptions(q=1, max=1))

    @property
    def root(self):
        return self.root_ctrl_le.text()

    @property
    def track(self):
        return self.track_ctrl_le.text()

    @property
    def all_controls(self):
        return self.textEdit.toPlainText().split('\n')

    @property
    def skip_frames(self):
        return self.spinBox.value()

    def q_r(self, name):
        return cmds.xform(name, q=1, ws=1, ro=1)

    def q_t(self, name):
        return cmds.xform(name, q=1, ws=1, t=1)

    def p_r(self, name, ro):
        return cmds.xform(name, ws=1, ro=ro)

    def p_t(self, name, t):
        return cmds.xform(name, ws=1, t=t)

    def input_root(self):
        self.root_ctrl_le.setText(cmds.ls(sl=1)[0])
        hip = ':'.join(cmds.ls(sl=1)[0].split(':')[:-1]) + ':CTL_Hips'
        if cmds.objExists(hip):
            self.track_ctrl_le.setText(hip)
        all_controls = [each.getParent().name() for each in pm.listRelatives(self.root, c=1, ad=1, type='nurbsCurve')
                        if each.getParent().isVisible()
                        ]
        self.textEdit.setText('\n'.join(all_controls))

    def bake_all_controls(self):
        controls_str = '{' + ','.join(['"'+each+'"' for each in self.all_controls]) + '}'
        bake_command = 'bakeResults -simulation true -t "%s:%s" -sampleBy %s -oversamplingRate 1 '\
                 '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '\
                 '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer false '\
                 '-minimizeRotation true -controlPoints false -shape true %s;' % (self.min_frame, self.max_frame,
                                                                                  self.skip_frames, controls_str)
        mel.eval(bake_command)

    def set_anim_curve_step(self):
        cmds.keyTangent(self.all_controls, ott='step')

    def bake_locator(self):
        self.locator = cmds.spaceLocator()[0]
        cmds.parentConstraint(self.track, self.locator, mo=0)
        bake_command = 'bakeResults -simulation true -t "%s:%s" -sampleBy 1 -oversamplingRate 1 '\
                 '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '\
                 '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer false '\
                 '-minimizeRotation true -controlPoints false -shape true "%s";' % (self.min_frame, self.max_frame,
                                                                                    self.locator)
        mel.eval(bake_command)
        pass

    def match_root(self):
        cmds.select(self.root, r=1)
        i = self.min_frame
        j = 0
        locator_transform_info = []
        # root_transform_info = []
        while 1:
            if i > self.max_frame:
                break
            cmds.currentTime(i)
            locator_t = self.q_t(self.locator)
            root_t = self.q_t(self.root)
            locator_transform_info.append(locator_t)
            # root_transform_info.append(root_t)
            if (i-self.min_frame) % self.skip_frames != 0:
                # 说明该帧不是关键帧
                pre_locator_t = locator_transform_info[j-1]
                # pre_root_t = root_transform_info[j-1]
                offset = [locator_t[0]-pre_locator_t[0], locator_t[1]-pre_locator_t[1], locator_t[2]-pre_locator_t[2]]
                current_root_t = [offset[0]+root_t[0], offset[1]+root_t[1], offset[2]+root_t[2]]
                self.p_t(self.root, current_root_t)
                mel.eval('SetKey;')
                # 该帧是空帧
                pass
            i += 1
            j += 1
        cmds.delete(self.locator)
        pass

    def bake_doit(self):
        self.bake_locator()
        self.bake_all_controls()
        self.set_anim_curve_step()
        self.match_root()
        pass










if __name__ == '__main__':
    win = CutAnimFrames()
    win.show()
