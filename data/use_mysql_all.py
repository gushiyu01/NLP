# coding=utf-8
import MySQLdb
import json

conn = MySQLdb.connect(
    db='politician_kb',
    host='172.16.12.57',
    user='root',
    password='root',
    charset='utf8'
)


cursor = conn.cursor()
# 准备查询语句 (如果数据量大，需要借助于分页查询)
sql = 'SELECT * FROM `USA_EN_INFO_1116`'
# 查询数据
cursor.execute(sql)
rows = cursor.fetchall()

entity_file = open('./entity_full.json', 'w', encoding='utf-8')


for row in rows:

    dic = {
        "mongo_id": "",
        "Entity_name": "",
        "Chinese_name": "",
        "English_text": "",
        "Chinese_text": "",
        "Entity_type": "human",
        "meta_type": "entity",
        "Subtype": "",
        "phone_number": "",
        "legal_form": "",
        "industry": "",
        "name": [],
        "population": [],
        "GDP": [],
        "area": [],
        "occupation": [],
        "name_in_native_language": [],
        "nickname": [],
        "country_of_citizenship": [],
        "place_of_birth": [],
        "date_of_birth": [],
        "date_of_death": [],
        "date_of_disappearance": [],
        "ethic_group": [],
        "religion": [],
        "military_rank": [],
        "military_branch": [],
        "member_of_political_party": [],
        "award_received": [],
        "email": [],
        "official_blog": [],
        "official_website": [],
        "birth_name": [],
        "short_name": [],
        "native_label": [],
        "headquarters_location": [],
        "inception": [],
        "member_count": [],
        "employees": [],
        "political_ideology": [],
        "official_name": [],
        "capital": [],
        "continent": [],
        "country": [],
        "located_in_or_next_to_body_of_water": [],
        "gini_coefficient": [],
        "coordinate_location": [],
        "local_dialing_code": [],
        "postal_code": [],
        "coat_of_arms_image": [],
        "vessel_class": [],
        "location_of_final_assembly": [],
        "total_produced": [],
        "first_flight": [],
        "service_entry": [],
        "service_retirement": [],
        "use": [],
        "cost": [],
        "muzz_levelocity": [],
        "length": [],
        "width": [],
        "height": [],
        "mass": [],
        "bore": [],
        "diameter": [],
        "wingspan": [],
        "conflict": [],
        "significant_event": [],
        "participant_of": [],
        "armament": [],
        "call_sign": [],
        "pennant_number": [],
        "image": [],
        "image_path": "",
        "dataset_tag": [],
        "district": "",
        "biography": "",
        "stats_attr.key": [],
        "stats_attr.value": [],
        "gender": "",
        "vital_node": 0,
        "abstract": "",
        "basic_experience": [],
        "position_experience": [],
        "education_experience": [],
        "index": "",
        "main_page": "",
        "media_type": "",
        "location": "",
        "爱好": "",
        "在世期": "",
        "join_time": "",
        "出生姓名": "",
        "人物": "",
        "洗礼日期": "",
        "母语人名": "",
        "传真号码": "",
        "成立或创建时间": "",
        "出生日期": "",
        "now_o": "",
        "history_o": "",
        "history": "",
        "账号姓名": "",
        "账号": "",
        "借贷标志": "",
        "重量": "",
        "交易类型": "",
        "图片": "",
        "身高": "",
        "最西点": "",
        "language": "",
        "net_name": "",
        "edu1_time": "",
        "work1_o": "",
        "hometown": "",
        "work1_time": "",
        "edu3_time": "",
        "professional": "",
        "edu1_degree": "",
        "edu1": "",
        "edu2_degree": "",
        "edu3_degree": "",
        "edu3": "",
        "school": "",
        "edu2": "",
        "edu2_time": "",
        "交易网点名称": "",
        "label1": "",
        "label": [],
        "交易结果": "",
        "交易时间": "",
        "交易流水号": "",
        "node_id": "",
        "current_official_position": [],
        "academic_degree": [],
        "member_of": [],
        "residence": [],
        "Subsubtype": "",
        "create_time": "",
        "_id": "",
        "education_background": [],
        "address": [],
        "professional_division": [],
        "ancestral_home": [],
        "political_faction": [],
        "fax": [],
        "academic_major": [],
        "duty": [],
        "political_leaning": [],
        "海拔": "",
        "fb账号名称": "",
        "fb账号ID": "",
        "地理形状": "",
        "地理坐标": ""
    }

    dic['mongo_id'] = row[0]
    dic['Entity_name'] = '' if ( row[1] == None ) else row[1]
    dic['Chinese_name'] = '' if ( row[2] == None ) else row[2]

    dic['image_path'] = '' if ( row[3] == None ) else row[3]
    dic['English_text'] = '' if ( row[4] == None ) else row[4]
    dic['Chinese_text'] = '' if ( row[5] == None ) else row[5]
    dic['residence'] = '' if ( row[6] == None ) else [row[6]]
    dic['phone_number'] = '' if ( row[7] == None ) else row[7]
    dic['occupation'] = [] if ( row[8] == None ) else eval(row[8])
    dic['current_official_position'] = [] if ( row[9] == None ) else [row[9]]
    dic['name_in_native_language'] = [] if ( row[10] == None ) else [row[10]]
    # alias_name 11
    dic['nickname'] = [] if ( row[11] == None ) else eval(row[11])
    # chinese_alias 12
    dic['birth_name'] = [] if ( row[13] == None ) else [row[13]]
    dic['gender'] = row[14]
    dic['country_of_citizenship'] = [] if ( row[15] == None ) else eval(row[15])
    dic['ethic_group'] = [] if ( row[16] == None ) else [row[16]]  # ethnic_group
    dic['religion'] = [] if ( row[17] == None ) else [row[17]]
    # father 18
    # mother 19
    # spouse 20
    # children 21
    # sibling 22
    dic['date_of_birth'] = [] if ( row[23] == None ) else [row[23]]
    dic['place_of_birth'] = [] if ( row[24] == None ) else [row[24]]
    dic['academic_degree'] = [] if ( row[25] == None ) else [row[25]]
    dic['member_of'] = [] if ( row[26] == None ) else [row[26]]
    # employer 27
    dic['award_received'] = [] if ( row[28] == None ) else [row[28]]
    dic['military_rank'] = [] if ( row[29] == None ) else [row[29]]
    dic['military_branch'] = [] if ( row[30] == None ) else [row[30]]
    dic['member_of_political_party'] = [] if ( row[31] == None ) else [row[31]]
    dic['email'] = [] if ( row[32] == None ) else [row[32]]
    # Vote_Smart_ID 33
    dic['official_blog'] = [] if ( row[34] == None ) else [row[34]]
    dic['official_website'] = [] if ( row[35] == None ) else [row[35]]
    # twitter_username 36
    dic['fb账号ID'] = '' if ( row[10] == None ) else row[37]
    # linedin_in 38

    json.dump(dic, entity_file, ensure_ascii=False)
    entity_file.write('\n')
print('over')
entity_file.close()





