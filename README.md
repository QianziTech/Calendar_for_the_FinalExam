# Calendar_for_importing the Final Exam

Tips:You can get  <a href='./manual/English version.md'>English version</a> of the page here.

### 从教务系统获取您的期末考试安排，并将其导入至您的日历软件

#### What's Function?

- 关联校区位置（默认为湖州师范学院/湖州学院的校区关联关系，但您可以通过修改位于 <code>/modules</code>文件夹下的JSON文件来适配您自己的学校的校区关联关系)。
- 筛选考试地点，科目，时间。
- 提前一小时通知您。

#### How to start?

为了导入您的期末考试数据并生成ICS文件，您需要先下载您的Excel版期末考试数据。

如果您的教务系统是正方教务系统，请按以下步骤操作：

<ol>
    <li> 前往教务系统并切换到考试信息页面:</li>
    <br>
    <li> 点击“考试信息查询。</li>
    <img src='manual_imgs/1.png'></img>
    <li> 点击”导出“并选择“Excel格式”。</li>
    <img src='manual_imgs/2.png'></img>
    <li> 下载此存储库到您的电脑并解压。</li>
    <li> 确保您的电脑具有Python 3.12以上版本。在此程序存储文件夹中打开终端，运行以下命令：<code>pip install -r requirements.txt</code></li>
    <li> 运行main.py，并按提示导入您在步骤3中得到的excel文件。</li>
    <li> 您会在此程序运行路径下的文件夹 <code>result</code> 得到ICS日历文件。</li>
    <li> 将这个ICS文件导入进您的日历App.
</ol>

### (此程序仍在完善，如有异常，敬请Issue提出！)
