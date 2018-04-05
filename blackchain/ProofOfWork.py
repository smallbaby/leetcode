# -*- coding: utf-8 -*-
# __author__ = 'kai.zhang01'
# create date = 2018/03/26
import time
from Block import _hash
TARGET_BITS = 20 # 难度目标值

class ProofOfWork:

    def __init__(self, block, target):
        '''

        :param block: 区块
        :param target: 难度
        '''

        self.block = block
        self.target = target

    @staticmethod
    def newProofOfWord(block):
        targetValue = 1 << (256 - TARGET_BITS)
        return ProofOfWork(block, targetValue)


    def prepareData(self, nonce):
        pass

    def run(self):
        nonce = 0
        shaHex = ''
        print self.block.data
        t0 = time.time()
        while nonce < (2<<64-1):
            data = self.prepareData(nonce)
            shaHex = _hash(data)


if __name__ == '__main__':
    print 1111