from flask import request, jsonify
from flask_restx import Resource, Api, Namespace, fields
import numpy as np
import pandas as pd
import os
import os.path as path
from PIL import Image
import requests

def predict_result(data):
    #예측 수행 라벨 값 출력 -> 문자열로 처리 필요
        
    output = (0)
    return output
    
def output_process(output):    
    #라벨링 된 값을 문자열로 변환    
    
    output_processed = ("충북 영동군 영동읍 계산리 653-12")    
    return output_processed



Recommend_Model = Namespace(
    name="Recommend Model",
    description="RecommendATION APP에서 사용할 추천 모델 API.",
)


RM_Input = Recommend_Model.model('Recommend Model Input', {  # Model 객체 생성
    'input_data' : fields.List(fields.Integer, required=True\
        ,default=[0,0,0,0,0,0,0,0,0]\
        ,description='[성별(AGE), \
                        여행동반자관계(TCR),  \
                        동반자연령대(AGE), \
                        여행동기(TMT),  \
                        여행스타일(TSY),  \
                        미션(MIS),  \
                        소득(INC), \
                        숙소유형(HTY), \
                        미션(MIS)]'\
        ,example="[0,0,0,0,0,0,0,0,0]")
})

RM_Recommend = Recommend_Model.model('RM Recommend output', {
    'output_data': fields.List(fields.String, description='추천도에 따른 내림차순 방문지주소 배열',
                                 required=True,
                                 example="[충북 영동군 영동읍 계산리 653-12,...]",
                                 default=["충북 영동군 영동읍 계산리 653-12"])
})

# RM_Recommend = Recommend_Model.inherit('RM Recommend output', RM_Input, {
#     'output_data': fields.Raw(description='tuple : (방문지명, \
#                                  방문지주소,  \
#                                  방문지유형)',
#                                  required=True,
#                                  example="3000냥밥집, \
#                                  충북 영동군 영동읍 계산리 653-12, 식당")
# })


# @Recommend_Model.route('/', methods=['GET','POST'])
@Recommend_Model.route('/Recommend', methods=['GET','POST'])
class RMPost(Resource):
    @Recommend_Model.expect(RM_Input)
    @Recommend_Model.response(201,"Success", RM_Recommend)
    def post(self):
        """Model이 예측을 수행하고 output을 처리과정을 거쳐서 다른 서버로 전송."""
        if request.method == 'POST':
            # received_data = request.json.get('input_data')
            # received_data = Recommend_Model.payload['input_data']
            received_data = request.json
            
            prediction_result = predict_result(received_data) 
                # 예측을 수행
                # output라벨링된 값이므로 라벨링값을 실제 명칭으로 변환
            processed_output = output_process(prediction_result) 
                # 데이터를 명칭값으로 변환

            return jsonify(np.array(processed_output).tolist())
            # return processed_output