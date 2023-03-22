# 打印堆栈信息

## 1. python打印堆栈

- 代码示例：

  ```python
  import traceback
  
  def PrintTraceMsg():
      oStack = traceback.extract_stack()
      for sFileName, iLineNo, sName, sLookUpLine in oStack[:-1]:
          print("File '%s', line'%s', in '%s', look '%s'" % (sFileName, iLineNo, sName, sLookUpLine))
  ```

  
