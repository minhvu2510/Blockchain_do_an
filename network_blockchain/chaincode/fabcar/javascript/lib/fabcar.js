/*
 * SPDX-License-Identifier: Apache-2.0
 */

'use strict';

const { Contract } = require('fabric-contract-api');

class FabCar extends Contract {

    async initLedger(ctx) {
        console.info('============= START : Initialize Ledger ===========');
        const cars = [
            {
                HoTen: 'Nguyễn Minh Vũ',
                GioiTinh: "Nam",
                DiaChi: 'Hải Dương',
                MaDuThi:'K20THPT100',
                NgaySinh: '25/10/2002',
                CMT: '142887654',
                KT: "A,D",
                BaiLam: {Anh: {MaDe: 'A8023470024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Toan: {MonThi:'Toan',MaDe: 'T8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Ly: {MonThi:'Ly',MaDe: 'L8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Hoa: {MonThi:'Hoa',MaDe: 'H8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'}
                },
                Diem: {Toan: 0, Ly: 0, Hoa: 0, Anh: 0}
            },
            {
                HoTen: 'Nguyễn Thanh Hải',
                GioiTinh: "Nam",
                DiaChi: 'Ninh Bình',
                MaDuThi:'K20THPT113',
                NgaySinh: '29/01/2002',
                CMT: '266239030',
                KT: "A,D",
                BaiLam: {Anh: {MaDe: 'A8096834325',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Toan: {MonThi:'Toan',MaDe: 'T8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Ly: {MonThi:'Ly',MaDe: 'L8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Hoa: {MonThi:'Hoa',MaDe: 'H8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'}
                },
                Diem: {Toan: 0, Ly: 0, Hoa: 0, Anh: 0}
            },
            {
                HoTen: 'Trần Minh Giang',
                GioiTinh: "Nam",
                DiaChi: 'Ninh Bình',
                MaDuThi:'K20THPT114',
                NgaySinh: '22/10/2002',
                CMT: '677243620',
                KT: "A,D",
                BaiLam: {Anh: {MaDe: 'A8096899926',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Toan: {MonThi:'Toan',MaDe: 'T8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Ly: {MonThi:'Ly',MaDe: 'L8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'},
                Hoa: {MonThi:'Hoa',MaDe: 'H8096870024',Ans1: 'E',Ans2: 'E',Ans3: 'E',Ans4: 'E',
                Ans5: 'E',Ans6: 'E',Ans7: 'E',Ans8: 'E',
                Ans9: 'E',Ans10: 'E', Ans11: 'E',Ans12: 'E'}
                },
                Diem: {Toan: 0, Ly: 0, Hoa: 0, Anh: 0}
            }
        ];

        for (let i = 0; i < cars.length; i++) {
            cars[i].docType = 'can';
            await ctx.stub.putState('THPTQG' + i, Buffer.from(JSON.stringify(cars[i])));
            console.info('Added <--> ', cars[i]);
        }
        console.info('============= END : Initialize Ledger ===========');
    }

    // async AnsryCar(ctx, carNumber) {
    async AnsryCandidate(ctx, candidateId) {
        const canAsBytes = await ctx.stub.getState(candidateId); // get the candidate from chaincode state
        if (!canAsBytes || canAsBytes.length === 0) {
            throw new Error(`${candidateId} does not exist`);
        }
        console.log(canAsBytes.toString());
        return canAsBytes.toString();
    }

    // async createCar(ctx, candidateId, HoTen, Diem, DiaChi, MaDe, MaDuThi, NgaySinh, CMT) {
    async createCandidate(ctx, candidateId, HoTen, GioiTinh, DiaChi, MaDuThi, NgaySinh, CMT, KT, BaiLam, Diem) {
        console.info('============= START : Create Candidate: Thêm thí sinh ===========');
        var Diem1 = JSON.parse(Diem.toString());
        var BaiLam1 = JSON.parse(BaiLam.toString());
        const candidate = {
            HoTen,
            GioiTinh,
            DiaChi,
            docType: 'can',
            MaDuThi,
            NgaySinh,
            CMT,
            DiaChi,
            NgaySinh,
            KT,
            BaiLam: BaiLam1,
            Diem: Diem1
        };

        await ctx.stub.putState(candidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END : Create Candidate ===========');
    }

    // async AnsryAllCars(ctx) {
    async AnsryAllCandidates(ctx) {
        const startKey = 'THPTQG0';
        const endKey = 'THPTQG99';

        const iterator = await ctx.stub.getStateByRange(startKey, endKey);

        const allResults = [];
        while (true) {
            const res = await iterator.next();

            if (res.value && res.value.value.toString()) {
                console.log(res.value.value.toString('utf8'));

                const Key = res.value.key;
                let Record;
                try {
                    Record = JSON.parse(res.value.value.toString('utf8'));
                } catch (err) {
                    console.log(err);
                    Record = res.value.value.toString('utf8');
                }
                allResults.push({ Key, Record });
            }
            if (res.done) {
                console.log('end of data');
                await iterator.close();
                console.info(allResults);
                return JSON.stringify(allResults);
            }
        }
    }

    // async changeCarOwner(ctx, carNumber, newOwner) {
    async changePoin(ctx, CandidateId, newPoin) {
        console.info('============= START : changePoin: Cập nhật điểm của thí sinh ===========');

        const canAsBytes = await ctx.stub.getState(CandidateId); // get the car from chaincode state
        if (!canAsBytes || canAsBytes.length === 0) {
            throw new Error(`${CandidateId} does not exist`);
        }
        const candidate = JSON.parse(canAsBytes.toString());
        // candidate.Diem = newPoin;
        candidate.Diem = JSON.parse(newPoin.toString());

        await ctx.stub.putState(CandidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END : changePoin ===========');
    }

    // async changeCarOwner(ctx, carNumber, newOwner) {
    async changeName(ctx, CandidateId, newName) {
        console.info('============= START : Cập nhật tên của thí sinh ===========');

        const canAsBytes = await ctx.stub.getState(CandidateId); // get the car from chaincode state
        if (!canAsBytes || canAsBytes.length === 0) {
            throw new Error(`${CandidateId} does not exist`);
        }
        const candidate = JSON.parse(canAsBytes.toString());
        candidate.HoTen = newName;

        await ctx.stub.putState(CandidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END  ===========');
    }
    async changeAddress(ctx, CandidateId, newAddress) {
        console.info('============= START : Cập nhật địa chỉ của thí sinh ===========');

        const canAsBytes = await ctx.stub.getState(CandidateId); // get the car from chaincode state
        if (!canAsBytes || canAsBytes.length === 0) {
            throw new Error(`${CandidateId} does not exist`);
        }
        const candidate = JSON.parse(canAsBytes.toString());
        candidate.DiaChi = newAddress;

        await ctx.stub.putState(CandidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END  ===========');
    }
    async changeIdentify(ctx, CandidateId, newIdentify) {
        console.info('============= START : Cập nhật số của thí sinh ===========');

        const canAsBytes = await ctx.stub.getState(CandidateId); // get the car from chaincode state
        if (!canAsBytes || canAsBytes.length === 0) {
            throw new Error(`${CandidateId} does not exist`);
        }
        const candidate = JSON.parse(canAsBytes.toString());
        candidate.CMT = newIdentify;

        await ctx.stub.putState(CandidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END : ===========');
    }
    async changeDate(ctx, CandidateId, NgaySinh) {
        console.info('============= START : Cập nhật số của thí sinh ===========');

        const canAsBytes = await ctx.stub.getState(CandidateId); // get the car from chaincode state
        if (!canAsBytes || canAsBytes.lAnhth === 0) {
            throw new Error(`${CandidateId} does not exist`);
        }
        const candidate = JSON.parse(canAsBytes.toString());
        candidate.NgaySinh = NgaySinh;

        await ctx.stub.putState(CandidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END : ===========');
    }
    async changeBaiLam(ctx, CandidateId, BaiLam) {
        console.info('============= START : Cập nhật BaiLam thí sinh ===========');

        const canAsBytes = await ctx.stub.getState(CandidateId); // get the car from chaincode state
        if (!canAsBytes || canAsBytes.lAnhth === 0) {
            throw new Error(`${CandidateId} does not exist`);
        }
        const candidate = JSON.parse(canAsBytes.toString());
        // candidate.BaiLam = BaiLam;
        candidate.BaiLam = JSON.parse(BaiLam.toString());

        await ctx.stub.putState(CandidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END : ===========');
    }
    async changeKT(ctx, CandidateId, KT) {
        console.info('============= START : Cập nhật BaiLam thí sinh ===========');

        const canAsBytes = await ctx.stub.getState(CandidateId); // get the car from chaincode state
        if (!canAsBytes || canAsBytes.lAnhth === 0) {
            throw new Error(`${CandidateId} does not exist`);
        }
        const candidate = JSON.parse(canAsBytes.toString());
        candidate.KT = KT;

        await ctx.stub.putState(CandidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END : ===========');
    }
    async changeGioiTinh(ctx, CandidateId, GioiTinh) {
        console.info('============= START : Cập nhật changeGioiTinh thí sinh ===========');

        const canAsBytes = await ctx.stub.getState(CandidateId); // get the car from chaincode state
        if (!canAsBytes || canAsBytes.lAnhth === 0) {
            throw new Error(`${CandidateId} does not exist`);
        }
        const candidate = JSON.parse(canAsBytes.toString());
        candidate.GioiTinh = GioiTinh;

        await ctx.stub.putState(CandidateId, Buffer.from(JSON.stringify(candidate)));
        console.info('============= END : ===========');
    }

}

module.exports = FabCar;
