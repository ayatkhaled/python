/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.12
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionopen2;
    QAction *actionsave;
    QAction *actionpause;
    QAction *actionopen;
    QAction *actionforward;
    QAction *actionbackword;
    QAction *actionfolder;
    QAction *actionStop;
    QWidget *centralwidget;
    QFrame *line;
    QStatusBar *statusbar;
    QToolBar *toolBar;
    QToolBar *toolBar_2;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(737, 483);
        actionopen2 = new QAction(MainWindow);
        actionopen2->setObjectName(QString::fromUtf8("actionopen2"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/icons8-open-file-folder-48.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionopen2->setIcon(icon);
        actionsave = new QAction(MainWindow);
        actionsave->setObjectName(QString::fromUtf8("actionsave"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/pause (1).png"), QSize(), QIcon::Normal, QIcon::Off);
        actionsave->setIcon(icon1);
        actionpause = new QAction(MainWindow);
        actionpause->setObjectName(QString::fromUtf8("actionpause"));
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/pause.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionpause->setIcon(icon2);
        actionopen = new QAction(MainWindow);
        actionopen->setObjectName(QString::fromUtf8("actionopen"));
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/play (1).png"), QSize(), QIcon::Normal, QIcon::Off);
        actionopen->setIcon(icon3);
        actionforward = new QAction(MainWindow);
        actionforward->setObjectName(QString::fromUtf8("actionforward"));
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/fast-forward.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionforward->setIcon(icon4);
        actionbackword = new QAction(MainWindow);
        actionbackword->setObjectName(QString::fromUtf8("actionbackword"));
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/back.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionbackword->setIcon(icon5);
        actionfolder = new QAction(MainWindow);
        actionfolder->setObjectName(QString::fromUtf8("actionfolder"));
        actionfolder->setIcon(icon);
        actionStop = new QAction(MainWindow);
        actionStop->setObjectName(QString::fromUtf8("actionStop"));
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/icons/stop.png"), QSize(), QIcon::Normal, QIcon::Off);
        actionStop->setIcon(icon6);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        line = new QFrame(centralwidget);
        line->setObjectName(QString::fromUtf8("line"));
        line->setGeometry(QRect(80, 180, 3, 61));
        line->setFrameShape(QFrame::VLine);
        line->setFrameShadow(QFrame::Sunken);
        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);
        toolBar = new QToolBar(MainWindow);
        toolBar->setObjectName(QString::fromUtf8("toolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, toolBar);
        toolBar_2 = new QToolBar(MainWindow);
        toolBar_2->setObjectName(QString::fromUtf8("toolBar_2"));
        MainWindow->addToolBar(Qt::BottomToolBarArea, toolBar_2);

        toolBar->addAction(actionfolder);
        toolBar_2->addAction(actionopen);
        toolBar_2->addAction(actionpause);
        toolBar_2->addAction(actionStop);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        actionopen2->setText(QApplication::translate("MainWindow", "open2", nullptr));
        actionsave->setText(QApplication::translate("MainWindow", "save", nullptr));
#ifndef QT_NO_TOOLTIP
        actionsave->setToolTip(QApplication::translate("MainWindow", "save", nullptr));
#endif // QT_NO_TOOLTIP
        actionpause->setText(QApplication::translate("MainWindow", "pause", nullptr));
        actionopen->setText(QApplication::translate("MainWindow", "open", nullptr));
        actionforward->setText(QApplication::translate("MainWindow", "forward", nullptr));
#ifndef QT_NO_TOOLTIP
        actionforward->setToolTip(QApplication::translate("MainWindow", "Forward", nullptr));
#endif // QT_NO_TOOLTIP
        actionbackword->setText(QApplication::translate("MainWindow", "backword", nullptr));
        actionfolder->setText(QApplication::translate("MainWindow", "folder", nullptr));
#ifndef QT_NO_TOOLTIP
        actionfolder->setToolTip(QApplication::translate("MainWindow", "open A File", nullptr));
#endif // QT_NO_TOOLTIP
        actionStop->setText(QApplication::translate("MainWindow", "Stop", nullptr));
#ifndef QT_NO_TOOLTIP
        actionStop->setToolTip(QApplication::translate("MainWindow", "Stop", nullptr));
#endif // QT_NO_TOOLTIP
        toolBar->setWindowTitle(QApplication::translate("MainWindow", "toolBar", nullptr));
        toolBar_2->setWindowTitle(QApplication::translate("MainWindow", "toolBar_2", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
