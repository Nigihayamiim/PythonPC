# ���Ҫ�������ļ�������

data = input("��������Ҫ�����ļ����ļ���:")
# ��ȡҪ�������ļ����ļ�����
data.rfind('.')
# ��ȡҪ�������ļ�����,���洢
f = open(data, 'rb')
line = f.readlines()
f.close()

# �������ļ�������
copy_data = input('���������ļ�������:')
# �������ļ���д�뿽�����ļ�����
f = open('copy_a', 'wb')
f.writelines(line)
f.close()
