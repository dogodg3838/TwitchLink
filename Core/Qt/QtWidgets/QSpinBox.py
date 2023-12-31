from PyQt6 import QtWidgets


class _QSpinBox_Patcher(QtWidgets.QSpinBox):
    def setValueSilent(self, value: int) -> None:
        self.blockSignals(True)
        self.setValue(value)
        self.blockSignals(False)
QtWidgets.QSpinBox.setValueSilent = _QSpinBox_Patcher.setValueSilent #Direct Attribute Patch - [Info] Affects all embedded objects