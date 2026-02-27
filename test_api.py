"""API功能验证脚本"""
import requests
import sys

def test_api_endpoints():
    """测试API端点功能"""
    base_url = "http://localhost:8000"
    
    print("🔍 正在测试API端点...")
    
    # 测试根路径
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ 根路径端点正常")
        else:
            print(f"❌ 根路径端点异常，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ 根路径端点连接失败: {e}")
    
    # 测试健康检查
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            print("✅ 健康检查端点正常")
        else:
            print(f"❌ 健康检查端点异常，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ 健康检查端点连接失败: {e}")
    
    # 测试API健康检查
    try:
        response = requests.get(f"{base_url}/api/v1/health")
        if response.status_code == 200:
            print("✅ API健康检查端点正常")
        else:
            print(f"❌ API健康检查端点异常，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ API健康检查端点连接失败: {e}")
    
    # 测试API信息端点
    try:
        response = requests.get(f"{base_url}/api/v1/info")
        if response.status_code == 200:
            print("✅ API信息端点正常")
        else:
            print(f"❌ API信息端点异常，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ API信息端点连接失败: {e}")

if __name__ == "__main__":
    test_api_endpoints()
    print("\n🎉 API功能验证完成!")