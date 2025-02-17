import requests

BASE_URL = "https://petstore.swagger.io/v2"

def test_get_inventory():
    """Тест получения списка товаров на складе"""
    response = requests.get(f"{BASE_URL}/store/inventory")
    assert response.status_code == 200
    print("✅ GET /store/inventory - OK")

def test_get_pet_by_id(pet_id):
    """Тест получения информации о товаре по ID"""
    response = requests.get(f"{BASE_URL}/pet/{pet_id}")
    if response.status_code == 200:
        print(f"✅ GET /pet/{pet_id} - OK: {response.json()}")
    elif response.status_code == 404:
        print(f"⚠️ GET /pet/{pet_id} - Not Found")
    else:
        print(f"❌ GET /pet/{pet_id} - Unexpected Error")

def test_add_pet():
    """Тест добавления нового товара"""
    new_pet = {
        "id": 999,
        "name": "Test Dog",
        "status": "available"
    }
    response = requests.post(f"{BASE_URL}/pet", json=new_pet)
    assert response.status_code == 200
    print("✅ POST /pet - OK")

def test_update_pet():
    """Тест обновления информации о товаре"""
    updated_pet = {
        "id": 999,
        "name": "Updated Test Dog",
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=updated_pet)
    assert response.status_code == 200
    print("✅ PUT /pet - OK")

def test_delete_pet(pet_id):
    """Тест удаления товара"""
    response = requests.delete(f"{BASE_URL}/pet/{pet_id}")
    if response.status_code == 200:
        print(f"✅ DELETE /pet/{pet_id} - OK")
    else:
        print(f"❌ DELETE /pet/{pet_id} - Failed")

if __name__ == "__main__":
    test_get_inventory()
    test_get_pet_by_id(999)  # Проверяем, есть ли тестовый товар
    test_add_pet()
    test_get_pet_by_id(999)  # Проверяем после добавления
    test_update_pet()
    test_get_pet_by_id(999)  # Проверяем после обновления
    test_delete_pet(999)
    test_get_pet_by_id(999)  # Проверяем после удаления
