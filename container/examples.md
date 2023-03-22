# 容器工具

## 1. 一种限量的容器

- 具体业务场景中，我们需要需要不断判断当前数据是否处理完成，一个可行的方法就是，确定了最后输出的“数据量”，例如最后会有5条数据，那么就将这个容器大小设置为5，当容器满时，表示处理完毕。

- 框架示例：

  ```python
  class CContainer:
      def __init__(self, iVolume: int):
          self.m_Elems: List = []  # 这里以list为例存储数据，具体可以根据业务需求进行调整
          self.m_Volume: int = iVolume  # 记录需要处理的数据个数
  
      def AddElem(self, oElem):
          self.m_Elems.append(oElem)
  
      def GetElems(self) -> List:
          return self.m_Elems
  
      def CheckFull(self) -> bool:
          return len(self.m_Elems) == self.m_Volume
  ```

  

