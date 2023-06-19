from typing import List
from fastapi import FastAPI, status, HTTPException, Depends
from database import Base, engine, SessionLocal
from datetime import datetime
from sqlalchemy.orm import Session
import models
import schemas
 
Base.metadata.create_all(engine) # Create the database
 
# Initialize app
app = FastAPI()
 
# Helper function to get database session
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

# ===============================AppUser=============================================
@app.get("/app-users", response_model = List[schemas.AppUser], tags=["users ユーザー"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    users_list = session.query(models.AppUser).all() # get all users items
 
    return users_list 


@app.get("/app-users/{id}", response_model=schemas.AppUser, tags=["users ユーザー"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    users = session.query(models.AppUser).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not users:
        raise HTTPException(status_code=404, detail=f"users item with id {id} not found")
 
    return users
 
@app.post("/app-users", response_model=schemas.AppUser, status_code=status.HTTP_201_CREATED, tags=["users ユーザー"])
def ユーザーの作成(users: schemas.AppUserCreate, session: Session = Depends(get_session)):
 
    usersdb = models.AppUser(
        name=users.name,
        email=users.email,
        password=users.password,
        birth=users.birth,
        age=users.age,
        gender=users.gender,
        quest_role=users.quest_role,
        family=users.family,
        last_login=datetime.today(),
        createdAt=datetime.today(),
        updatedAt=datetime.today(),
        publishedAt=datetime.today()
    )
 
    session.add(usersdb)
    session.commit()
    session.refresh(usersdb)
 
    return usersdb
 
 
@app.put("/app-users/{id}", response_model=schemas.AppUser, tags=["users ユーザー"])
def 特定のユーザーの更新(id: int, users: schemas.AppUserCreate, session: Session = Depends(get_session)):
    # Check if the users item with the given id exists
    existing_users = session.query(models.AppUser).get(id)
    if not existing_users:
        raise HTTPException(status_code=404, detail=f"users item with id {id} not found")

    # Update the attributes of the existing_users with the values from the users parameter
    existing_users.name = users.name
    existing_users.email = users.email
    existing_users.password = users.password
    existing_users.birth = users.birth
    existing_users.age = users.age
    existing_users.gender = users.gender
    existing_users.quest_role = users.quest_role
    existing_users.family = users.family

    session.commit()
    session.refresh(existing_users)

    return existing_users
 
@app.delete("/app-users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users ユーザー"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    users = session.query(models.AppUser).get(id)
 
    # if users item with given id exists, delete it from the database. Otherwise raise 404 error
    if users:
        session.delete(users)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"users item with id {id} not found")
 
    return None

# ===============================Profile=============================================
@app.get("/profiles", response_model = List[schemas.Profile], tags=["profiles プロファイル"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    profile_list = session.query(models.Profile).all() # get all profile items
 
    return profile_list 


@app.get("/profiles/{id}", response_model=schemas.Profile, tags=["profiles プロファイル"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    profile = session.query(models.Profile).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not profile:
        raise HTTPException(status_code=404, detail=f"profile item with id {id} not found")
 
    return profile
 
@app.post("/profiles", response_model=schemas.Profile, status_code=status.HTTP_201_CREATED, tags=["profiles プロファイル"])
def ユーザーの作成(profile: schemas.ProfileCreate, session: Session = Depends(get_session)):
 
    profiledb = models.Profile(
        name=profile.name,
        image=profile.image,
        content=profile.content
    )
 
    session.add(profiledb)
    session.commit()
    session.refresh(profiledb)
 
    return profiledb
 
 
@app.put("/profiles/{id}", response_model=schemas.Profile, tags=["profiles プロファイル"])
def 特定のユーザーの更新(id: int, profile: schemas.ProfileCreate, session: Session = Depends(get_session)):
    # Check if the profile item with the given id exists
    existing_profile = session.query(models.Profile).get(id)
    if not existing_profile:
        raise HTTPException(status_code=404, detail=f"profile item with id {id} not found")

    # Update the attributes of the existing_profile with the values from the profile parameter
    existing_profile.name = profile.name
    existing_profile.image = profile.image
    existing_profile.content = profile.content

    session.commit()
    session.refresh(existing_profile)

    return existing_profile
 
@app.delete("/profiles/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["profiles プロファイル"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    profile = session.query(models.Profile).get(id)
 
    # if profile item with given id exists, delete it from the database. Otherwise raise 404 error
    if profile:
        session.delete(profile)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"profile item with id {id} not found")
 
    return None

# ===============================Family=============================================
@app.get("/families", response_model = List[schemas.Family], tags=["families 家族"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    family_list = session.query(models.Family).all() # get all family items
 
    return family_list 


@app.get("/families/{id}", response_model=schemas.Family, tags=["families 家族"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    family = session.query(models.Family).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not family:
        raise HTTPException(status_code=404, detail=f"family item with id {id} not found")
 
    return family
 
@app.post("/families", response_model=schemas.Family, status_code=status.HTTP_201_CREATED, tags=["families 家族"])
def ユーザーの作成(family: schemas.FamilyCreate, session: Session = Depends(get_session)):
 
    familydb = models.Family(
        name=family.name,
        createdAt=datetime.today(),
        updatedAt=datetime.today()
    )
 
    session.add(familydb)
    session.commit()
    session.refresh(familydb)
 
    return familydb
 
 
@app.put("/families/{id}", response_model=schemas.Family, tags=["families 家族"])
def 特定のユーザーの更新(id: int, family: schemas.FamilyCreate, session: Session = Depends(get_session)):
    # Check if the family item with the given id exists
    existing_family = session.query(models.Family).get(id)
    if not existing_family:
        raise HTTPException(status_code=404, detail=f"family item with id {id} not found")

    # Update the attributes of the existing_family with the values from the family parameter
    existing_family.name=family.name

    session.commit()
    session.refresh(existing_family)

    return existing_family
 
@app.delete("/families/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["families 家族"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    family = session.query(models.Family).get(id)
 
    # if family item with given id exists, delete it from the database. Otherwise raise 404 error
    if family:
        session.delete(family)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"family item with id {id} not found")
 
    return None

# ===============================Post=============================================
@app.get("/posts", response_model = List[schemas.Post], tags=["posts"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    post_list = session.query(models.Post).all() # get all post items
 
    return post_list 


@app.get("/posts/{id}", response_model=schemas.Post, tags=["posts"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    post = session.query(models.Post).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not post:
        raise HTTPException(status_code=404, detail=f"post item with id {id} not found")
 
    return post
 
@app.post("/posts", response_model=schemas.Post, status_code=status.HTTP_201_CREATED, tags=["posts"])
def ユーザーの作成(post: schemas.PostCreate, session: Session = Depends(get_session)):
 
    postdb = models.Post(
        user=post.user,
        kids=post.kids,
        content=post.content,
        image_url=post.image_url,
        like=post.like,
        createdAt=datetime.today(),
        updatedAt=datetime.today(),
        publishedAt=datetime.today()
    )
 
    session.add(postdb)
    session.commit()
    session.refresh(postdb)
 
    return postdb
 
 
@app.put("/posts/{id}", response_model=schemas.Post, tags=["posts"])
def update_post(id: int, post: schemas.PostCreate, session: Session = Depends(get_session)):
    # Check if the post item with the given id exists
    existing_post = session.query(models.Post).get(id)
    if not existing_post:
        raise HTTPException(status_code=404, detail=f"Post item with id {id} not found")

    # Update the attributes of the existing_post with the values from the post parameter
    existing_post.user = post.user
    existing_post.kids = post.kids
    existing_post.content = post.content
    existing_post.image_url = post.image_url
    existing_post.like = post.like

    session.commit()
    session.refresh(existing_post)

    return existing_post
 
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["posts"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    post = session.query(models.Post).get(id)
 
    # if post item with given id exists, delete it from the database. Otherwise raise 404 error
    if post:
        session.delete(post)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"post item with id {id} not found")
 
    return None


# ===============================Comment=============================================
@app.get("/comments", response_model = List[schemas.Comment], tags=["comments"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    comment_list = session.query(models.Comment).all() # get all Comment items
 
    return comment_list 


@app.get("/comments/{id}", response_model=schemas.Comment, tags=["comments"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    comment = session.query(models.Comment).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not comment:
        raise HTTPException(status_code=404, detail=f"comment item with id {id} not found")
 
    return comment
 
@app.post("/comments", response_model=schemas.Comment, status_code=status.HTTP_201_CREATED, tags=["comments"])
def ユーザーの作成(comment: schemas.CommentCreate, session: Session = Depends(get_session)):
 
    commentdb = models.Comment(
        parent_id = comment.parent_id,
        post_id = comment.post_id,
        user_id = comment.user_id,
        content = comment.content,
        createdAt= datetime.today()
    )
 
    session.add(commentdb)
    session.commit()
    session.refresh(commentdb)
 
    return commentdb
 
 
@app.put("/comments/{id}", response_model=schemas.Comment, tags=["comments"])
def update_post(id: int, comment: schemas.CommentCreate, session: Session = Depends(get_session)):
    # Check if the comment item with the given id exists
    existing_comment = session.query(models.Comment).get(id)
    if not existing_comment:
        raise HTTPException(status_code=404, detail=f"Comment item with id {id} not found")

    # Update the attributes of the existing_comment with the values from the comment parameter
    existing_comment.parent_id = comment.parent_id
    existing_comment.post_id = comment.post_id
    existing_comment.user_id = comment.user_id
    existing_comment.content = comment.content

    session.commit()
    session.refresh(existing_comment)

    return existing_comment
 
@app.delete("/comments/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["comments"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    comment = session.query(models.Comment).get(id)
 
    # if comment item with given id exists, delete it from the database. Otherwise raise 404 error
    if comment:
        session.delete(comment)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"comment item with id {id} not found")
 
    return None

 
# ===============================Tree=============================================
@app.get("/trees", response_model = List[schemas.Tree], tags=["trees"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    tree_list = session.query(models.Tree).all() # get all Tree items
 
    return tree_list 


@app.get("/trees/{id}", response_model=schemas.Tree, tags=["trees"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    tree = session.query(models.Tree).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not tree:
        raise HTTPException(status_code=404, detail=f"tree item with id {id} not found")
 
    return tree
 
@app.post("/trees", response_model=schemas.Tree, status_code=status.HTTP_201_CREATED, tags=["trees"])
def ユーザーの作成(tree: schemas.TreeCreate, session: Session = Depends(get_session)):
 
    treedb = models.Tree(
        growth_stage = tree.growth_stage,
        quest = tree.quest,
        watering = datetime.today()
    )
 
    session.add(treedb)
    session.commit()
    session.refresh(treedb)
 
    return treedb
 
 
@app.put("/trees/{id}", response_model=schemas.Tree, tags=["trees"])
def update_post(id: int, tree: schemas.TreeCreate, session: Session = Depends(get_session)):
    # Check if the tree item with the given id exists
    existing_tree = session.query(models.Tree).get(id)
    if not existing_tree:
        raise HTTPException(status_code=404, detail=f"Tree item with id {id} not found")

    # Update the attributes of the existing_tree with the values from the tree parameter
    existing_tree.growth_stage = tree.growth_stage
    existing_tree.quest = tree.quest

    session.commit()
    session.refresh(existing_tree)

    return existing_tree
 
@app.delete("/trees/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["trees"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    tree = session.query(models.Tree).get(id)
 
    # if tree item with given id exists, delete it from the database. Otherwise raise 404 error
    if tree:
        session.delete(tree)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"tree item with id {id} not found")
 
    return None

 
# ===============================QuestType=============================================
@app.get("/quest_types", response_model = List[schemas.QuestType], tags=["quest_types"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    questtype_list = session.query(models.QuestType).all() # get all QuestType items
 
    return questtype_list 


@app.get("/quest_types/{id}", response_model=schemas.QuestType, tags=["quest_types"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    questtype = session.query(models.QuestType).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not questtype:
        raise HTTPException(status_code=404, detail=f"questtype item with id {id} not found")
 
    return questtype
 
@app.post("/quest_types", response_model=schemas.QuestType, status_code=status.HTTP_201_CREATED, tags=["quest_types"])
def ユーザーの作成(questtype: schemas.QuestTypeCreate, session: Session = Depends(get_session)):
 
    questtypedb = models.QuestType(
        kinds = questtype.kinds,
        online = questtype.online
    )

    session.add(questtypedb)
    session.commit()
    session.refresh(questtypedb)
 
    return questtypedb
 
 
@app.put("/quest_types/{id}", response_model=schemas.QuestType, tags=["quest_types"])
def update_post(id: int, questtype: schemas.QuestTypeCreate, session: Session = Depends(get_session)):
    # Check if the questtype item with the given id exists
    existing_tree = session.query(models.QuestType).get(id)
    if not existing_tree:
        raise HTTPException(status_code=404, detail=f"QuestType item with id {id} not found")

    # Update the attributes of the existing_tree with the values from the questtype parameter
    existing_tree.kinds = questtype.kinds
    existing_tree.online = questtype.online

    session.commit()
    session.refresh(existing_tree)

    return existing_tree
 
@app.delete("/quest_types/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["quest_types"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    questtype = session.query(models.QuestType).get(id)
 
    # if questtype item with given id exists, delete it from the database. Otherwise raise 404 error
    if questtype:
        session.delete(questtype)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"questtype item with id {id} not found")
 
    return None

 
# ===============================Reward=============================================
@app.get("/rewards", response_model = List[schemas.Reward], tags=["rewards"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    reward_list = session.query(models.Reward).all() # get all Reward items
 
    return reward_list 


@app.get("/rewards/{id}", response_model=schemas.Reward, tags=["rewards"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    reward = session.query(models.Reward).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not reward:
        raise HTTPException(status_code=404, detail=f"reward item with id {id} not found")
 
    return reward
 
@app.post("/rewards", response_model=schemas.Reward, status_code=status.HTTP_201_CREATED, tags=["rewards"])
def ユーザーの作成(reward: schemas.RewardCreate, session: Session = Depends(get_session)):
 
    rewarddb = models.Reward(
        content = reward.content
    )

    session.add(rewarddb)
    session.commit()
    session.refresh(rewarddb)
 
    return rewarddb
 
 
@app.put("/rewards/{id}", response_model=schemas.Reward, tags=["rewards"])
def update_post(id: int, reward: schemas.RewardCreate, session: Session = Depends(get_session)):
    # Check if the reward item with the given id exists
    existing_reward = session.query(models.Reward).get(id)
    if not existing_reward:
        raise HTTPException(status_code=404, detail=f"Reward item with id {id} not found")

    # Update the attributes of the existing_reward with the values from the reward parameter
    existing_reward.content = reward.content

    session.commit()
    session.refresh(existing_reward)

    return existing_reward
 
@app.delete("/rewards/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["rewards"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    reward = session.query(models.Reward).get(id)
 
    # if reward item with given id exists, delete it from the database. Otherwise raise 404 error
    if reward:
        session.delete(reward)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"reward item with id {id} not found")
 
    return None

 
# ===============================Quest=============================================
@app.get("/quests", response_model = List[schemas.Quest], tags=["quests"])
def ユーザー一覧取得(session: Session = Depends(get_session)):
 
    quests_list = session.query(models.Quest).all() # get all quests items
 
    return quests_list 


@app.get("/quests/{id}", response_model=schemas.Quest, tags=["quests"])
def 特定のユーザーの取得(id: int, session: Session = Depends(get_session)):
 
    quests = session.query(models.Quest).get(id) # get item with the given id
 
    # check if id exists. If not, return 404 not found response
    if not quests:
        raise HTTPException(status_code=404, detail=f"quests item with id {id} not found")
 
    return quests
 
@app.post("/quests", response_model=schemas.Quest, status_code=status.HTTP_201_CREATED, tags=["quests"])
def ユーザーの作成(quests: schemas.QuestCreate, session: Session = Depends(get_session)):
 
    questsdb = models.Quest(
        content=quests.content,
        quest_kinds=quests.quest_kinds,
        completed=quests.completed
    )
 
    session.add(questsdb)
    session.commit()
    session.refresh(questsdb)
 
    return questsdb
 
 
@app.put("/quests/{id}", response_model=schemas.Quest, tags=["quests"])
def 特定のユーザーの更新(id: int, quests: schemas.QuestCreate, session: Session = Depends(get_session)):
    # Check if the quests item with the given id exists
    existing_quests = session.query(models.Quest).get(id)
    if not existing_quests:
        raise HTTPException(status_code=404, detail=f"quests item with id {id} not found")

    # Update the attributes of the existing_quests with the values from the quests parameter
    existing_quests.content=quests.content
    existing_quests.quest_kinds=quests.quest_kinds
    existing_quests.completed=quests.completed

    session.commit()
    session.refresh(existing_quests)

    return existing_quests
 
@app.delete("/quests/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["quests"])
def 特定のユーザーの削除(id: int, session: Session = Depends(get_session)):
 
    # get the given id
    quests = session.query(models.Quest).get(id)
 
    # if quests item with given id exists, delete it from the database. Otherwise raise 404 error
    if quests:
        session.delete(quests)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"quests item with id {id} not found")
 
    return None
 
