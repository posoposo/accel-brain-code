#!/user/bin/env python
# -*- coding: utf-8 -*-
import random
import bisect
from deeplearning.neuron_object import Neuron
from deeplearning.neuron.interface.output_layer_interface import OutputLayerInterface


class OutputNeuron(Neuron, OutputLayerInterface):
    '''
    出力層のニューロン
    '''

    # 活性度を二値にするか否かのフラグ
    __bernoulli_flag = False

    def get_bernoulli_flag(self):
        ''' getter '''
        if isinstance(self.__bernoulli_flag, bool) is False:
            raise TypeError()
        return self.__bernoulli_flag

    def set_bernoulli_flag(self, value):
        ''' setter '''
        if isinstance(value, bool) is False:
            raise TypeError()
        self.__bernoulli_flag = value

    bernoulli_flag = property(get_bernoulli_flag, set_bernoulli_flag)

    def __init__(self):
        '''
        バイアスを初期化する
        '''
        self.bias = round(random.random(), 3)

    def output_update_state(self, link_value):
        '''
        インターフェイス実現
        出力層の学習

        Args:
            link_value:      リンク先による入力値

        '''
        # 活性化の判定
        ''' selfのactivityではなく、結合しているニューロンからの入力を入れる '''
        output = self.activate(link_value)
        if self.bernoulli_flag is False:
            self.activity = output
        else:
            activated_flag = self.__decide_activation(output)
            if activated_flag:
                self.activity = 1.0
            else:
                self.activity = 0.0

    def update_bias(self, learning_rate):
        '''
        具象メソッド
        バイアスの調整

        Args:
            learning_rate:  学習率
        '''
        self.diff_bias += learning_rate * self.activity

    def __decide_activation(self, probabirity):
        '''
        二値の活性化判定

        Args:
            probabirity:    活性度

        Returns:
            true => 活性化 false => 非活性化
        '''
        probabirity_list, result_list = [probabirity, 1.0], [True, False]
        return result_list[bisect.bisect(probabirity_list, random.random())]

    def release(self):
        '''
        活性度を放出する

        Returns:
            活性度
        '''
        return self.activity
