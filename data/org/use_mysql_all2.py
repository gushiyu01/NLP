# coding=utf-8
import MySQLdb
import json
import time

conn = MySQLdb.connect(
    db='politician_kb',
    host='172.16.12.57',
    user='root',
    password='root',
    charset='utf8'
)

cursor = conn.cursor()
batch_size = 10000


def get_total_count():
    """
    分页查询获取总数量
    :return:
    """
    sql = "select count(*) from wiki_org_info"
    cursor.execute(sql)
    rst = cursor.fetchone()
    print(rst[0])
    if rst is None:
        return 0
    return rst[0]


def get_tweet_by_page(start, pagesize):
    """
    分页查询
    :param start:
    :param pagesize:
    :return:
    """
    sql = "select * from wiki_org_info limit %s offset %s "
    cursor.execute(sql, [pagesize, start])
    rst = cursor.fetchall()
    return rst


def limit_offset_query():
    """
    分页查询
    :return:
    """
    # 数据总量
    total_count = get_total_count()
    if total_count <= 0:
        return
    # 总页数
    total_page = total_count / batch_size
    # 开始时间
    start_time = time.time()
    # 遍历每一页
    for i in range(int(total_page) + 1):
        # 起始位置
        start = batch_size * i
        # 查询数据
        result_list = get_tweet_by_page(start, batch_size)
        if len(result_list) > 0:
            print('获取%s到%s数据成功' % (start, start + batch_size))

            entity_file = open('./data/entity_org_full_test.json', 'a+', encoding='utf-8')

            for row in result_list:

                dic = {
                    "mongo_id": "",
                    "Entity_name": "",
                    "Chinese_name": "",
                    "English_text": "",
                    "Chinese_text": "",
                    "Entity_type": "organization",
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
                dic['Entity_name'] = '' if (row[1] is None) else row[1]
                dic['Chinese_name'] = '' if (row[2] is None) else row[2]
                dic['English_text'] = '' if (row[3] is None) else row[3]
                dic['Chinese_text'] = '' if (row[4] is None) else row[4]
                # alias_name 5
                # chinese_alias 6
                dic['image'] = [] if (row[7] is 'None') else eval(row[7])
                dic['Subtype'] = '' if (row[8] is None) else row[8]
                dic['legal_form'] = '' if (row[9] is None) else row[9]
                dic['industry'] = '' if (row[10] is None) else row[10]
                dic['phone_number'] = '' if (row[11] is None) else row[11]
                dic['official_blog'] = [] if (row[12] is None) else [row[12]]
                dic['official_website'] = [] if (row[13] is None) else [row[13]]
                dic['email'] = [] if (row[14] is None) else [row[14]]
                dic['short_name'] = [] if (row[15] is None) else [row[15]]
                dic['native_label'] = [] if (row[16] is None) else [row[16]]
                dic['inception'] = [] if (row[17] is None) else [row[17]]
                dic['member_count'] = [] if (row[18] is None) else [row[18]]
                dic['headquarters_location'] = [] if (row[19] is None) else [row[19]]
                dic['employees'] = [] if (row[20] is None) else eval(row[20])
                dic['political_ideology'] = [] if (row[21] is None) else [row[21]]
                dic['official_name'] = [] if (row[22] is None) else [row[22]]
                dic['country'] = [] if (row[23] is None) else [row[23]]
                # founded_by 24
                # owned_by 25
                # chairperson 26
                # parent_organization 27
                # subsidiary 28
                # chief_executive_officer 29
                dic['fb账号ID'] = '' if (row[30] is None) else row[30]
                # Twitter_username 31
                json.dump(dic, entity_file, ensure_ascii=False)
                entity_file.write('\n')
            print('over')
            entity_file.close()
    print("耗时：", time.time() - start_time)


limit_offset_query()
