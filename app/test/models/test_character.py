import unittest
from .. import TestGroup

from app.main import db
from app.main.models.character import Character, Class, load_classes

class TestCharacter(TestGroup):
    
    def test_constructor(self):
        # Arrange
        name = "TestCharacter"
        level = 1
        user_id = 1
        class_name = "Buccaneer"
        
        # Act
        character = Character(
            name=name,
            level=level,
            user_id=user_id,
            class_name=class_name
        )
        
        # Assert
        self.assertEqual(name, character.name)
        self.assertEqual(level, character.level)
        self.assertEqual(class_name, character.class_name)
        self.assertEqual(user_id, character.user_id)
    
    def test_repr(self):
        # Arrange
        id = 0
        name = "TestCharacter"
        level = 1
        user_id = 1
        class_name = "Buccaneer"
        
        character = Character(
            id=id,
            name=name,
            level=level,
            user_id=user_id,
            class_name=class_name
        )
        
        # Act
        repr_str = repr(character)
        
        # Assert
        self.assertEqual("Character[id=0, name=TestCharacter, level=1, class_name=Buccaneer, user_id=1]", repr_str)