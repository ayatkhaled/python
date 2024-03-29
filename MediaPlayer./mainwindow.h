#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMediaPlayer>
#include <QVideoWidget>
#include <QFileDialog>
#include <QProgressBar>
#include <QSlider>
QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_actionpause_triggered();

    void on_actionopen_triggered();

    void on_actionfolder_triggered();

    void on_actionStop_triggered();

private:
    Ui::MainWindow *ui;
    QMediaPlayer *player;
    QVideoWidget *vw;
    QProgressBar *bar;
    QSlider *slider;
};
#endif // MAINWINDOW_H
