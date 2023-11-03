let isLoading = false

export const loadingFun = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() =>{
            resolve(isLoading = true);
        }, 1350)
    })
}