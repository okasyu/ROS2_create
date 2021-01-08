# 1.ロボットシステム学課題2について
第11回で作成したROS2のパッケージをベースに、オリジナリティーある改造をして、<br>
GitHubに置くこと。
 
# 2.使用した道具、開発環境について
・ラズベリーパイ4×1 <br>
・ubuntu 18.04 LTS<br>
・ROS2<br>

# 3.ROS2の改造について
サブスクライバであるlistener.pyの("Listen: %d %msg.data)の部分を変更し、<br>
インターネットで分岐やプログラムを終了させるコマンドを調べ、動画で作成した<br>
ローンチファイルのtalk_listen.launch.pyでパブリッシャのtalker.pyと<br>
サブスクライバのlistener.pyを実行させ、1.5秒ごとに宇宙世紀に存在した<br>
ガンダムの名前を表示させる。

# 4.改造したROS2を動かす手順について
1.git clone https://github.com/ryuichiueda/ros2_setup_scripts.git を行う。<br>
2.講義動画を見ながら、パブリッシャ、サブスクライバの実装やワークスペースの作成などいった<br>
  ROS2のパッケージを作っていく。<br>
3.~/ros2_ws/src/mypkg/mypkgのディレクトリでlistener.pyを改造する。<br>
4.cd ..,cd launch/を行い、~/ros2_ws/src/mypkg/launchのディレクトリで(cd ~/ros2_ws && colcon build )を実行する。<br>
5.cd ~/ros2_wsを行い、. install/setup.bashを実行する。<br>
6.ros2 launch mypkg talk_listen.launch.pyを実行する。<br>
7.一連の流れが終了したら、Ctrl+Cを実行する。<br>

# 5.ROS2を実際に動かしている動画について
こちらのURLからアクセスする。<br>
URL https://www.youtube.com/watch?v=JBuilzmpt6o　
 
# 6.調べたコマンドについて
こちらがpythonのコマンドを調べるにあたって使用したサイトのURLである。<br>
https://techacademy.jp/magazine/15831<br>
https://www.headboost.jp/python-else-if/<br>

 
 
 
 
 
 
