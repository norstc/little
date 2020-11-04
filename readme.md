### little 
for my all scripts

## python

使用python + selenium + genckodriver（火狐驱动器）+ firefox 构建一个自动化的确认测试平台（Automated Acceptance Test Platform)



python:  3.8.3



```shell
python --version
Python 3.8.3
```



genckodriver:

https://github.com/mozilla/geckodriver/releases/tag/v0.28.0

下载最新的zip包 geckodriver-v0.28.0-win64.zip ，然后解压，将路径 E:\tech\python\geckodriver-v0.28.0-win64 加到环境变量path



## autoit
使用pyautoit 调用autoit
使用pywinauto 帮助识别windows 
```shell script
pip install pyautoit
```

```python
import autoit

autoit.run("notepad.exe")
```
## shell
use curl to test
```shell script
curl -H 'content-type:text/plain' \
-d '{"interfaceName":"iopL0ActivityQuery","header":{"version":"1.0","timestamp":"1567578264704","digest":"YmYzNDA1ZWVlM2RkN2M1YmY0ZGNmNjg4YWE0NTc3M2Y=","conversationId":"1567578264704687757"},"data":{"servNum":"18320072562","provId":200,"iopChannelId":"1000027","iopOperationPositionId":"017052008513"}}' \
http://117.136.190.162:80/web-Center/iopService/straightQueryIOPActivity.do
```
result
```json
{"result":{"conversationId":"1567578264704687757","message":"成功","responseCode":"0000","productInfo":{"activityId":"YX0000000010092172020062904589","marketingType":"","src":"http://www.10086.cn/publiczone/uploadBaseDir/content/jpg/20200629/202006291048126974H3.jpg","price":"","markDesc":"广东测试0629b","name":"广东测试0629b","actionUrl":"http://www.10086.cn/?WT.ac_id=&WT.ac_id=1001_2200001_220000110002_YX0000000010092172020062904589_10_8513","picName":"","subActivityId":"YX0000000010092172020062904589_10_8513","provId":"200","contentType":"标准活动"}}}

```
## batch