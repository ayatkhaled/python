#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    player = new QMediaPlayer(this);
    vw= new QVideoWidget(this);
    player->setVideoOutput(vw);
    this->setCentralWidget(vw);
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_actionpause_triggered()
{
    player ->pause();
     ui->statusbar->showMessage("Paused");
}







void MainWindow::on_actionopen_triggered()
{
 player ->play();
  ui->statusbar->showMessage("Playing");
}




void MainWindow::on_actionfolder_triggered()
{
    QString filename =QFileDialog::getOpenFileName(this,"open a file","","Video File(* .avi,*.mpg,*.mp4)");
    on_actionpause_triggered();
    player->setMedia(QUrl::fromLocalFile(filename));
    on_actionopen_triggered();
}


void MainWindow::on_actionStop_triggered()
{

    player ->stop();
     ui->statusbar->showMessage("Stop");
}

