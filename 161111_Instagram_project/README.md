# 인스타그램 서비스 설계

인스타그램과 유사한 데이터베이스 구조를 설계하고, API를 제작해봅니다.

## DB 구조

**사용자 계정 (member.MyUser)**  

**Fields**

- username
- password
- last_name
- first_name
- img_profile
- like_photos
	- PhotoLike목록
- following_users (MTM Intermediate to self, symmetric False)
- block_users (MTM Intermediate to self, symmetric False)
	- 다른 MyUser와 Follower, Following, Block관계를 가져야 함

**Method**

friends() : 해당 유저와 서로 following한 user의 목록 리턴  
follow(user) : 해당 유저를 following하도록 함  
unfollow(user) : 해당 유저로의 following을 해제  
block(user): 해당 유저를 block하도록 함  
unblock(user): 해당 유저의 block을 해제한다  

	
**사진 (photo.Photo)**

- image (포스트 1개의 이미지파일)
- author (올린사람)
- content (포스트의 내용)
- tags (MTM PhotoTag) (태그 목록)

**사진 태그 (photo.PhotoTag)**

> 해시태그 형태로 동작

- title (태그명)


**사진 댓글 (photo.PhotoComment)**

- photo (해당 Photo)
- author (작성자)
- content (댓글내용)


**사진 좋아요 (photo.PhotoLike)**

- photo (해당 사진)
- user (좋아요 누른 유저)
- created_date (자동)


## API

설계해봅시다