import React from 'react';
import instagram from "../assets/instagram.png";
import github from "../assets/github.png";

export const Footer = () => {
    return <footer className='footer'>
        <ul className='ulFooter'>
            <li>
                <div>
                    <p>Redes:</p>
                    <ul className='ulRedes'>
                        <li>
                            <a href='https://github.com/Ulises-Rodriguez-809/React_JS_Coder_House.git' target='_blanck'>
                                <img src={github} alt='GitHub' />
                            </a>
                        </li>
                        <li>
                            <a href='https://instagram.com/ulirodriguez5?igshid=OGQ5ZDc2ODk2ZA==' target='_blanck'>
                                <img src={instagram} alt='Instagram' />
                            </a>
                        </li>
                    </ul>
                </div>
            </li>
            <li>
                <div className='mediosDePago'>
                    <p>Medios de pago:</p>
                    <ul>
                        <li>
                            <img src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/visa@2x.png" data-src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/visa@2x.png" className="icon-logo ls-is-cached lazyloaded" alt="visa" />
                        </li>
                        <li>
                            <img src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/mastercard@2x.png" data-src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/mastercard@2x.png" className="icon-logo ls-is-cached lazyloaded" alt="mastercard" />
                        </li>
                        <li>
                            <img src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/mercadopago@2x.png" data-src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/mercadopago@2x.png" className="icon-logo lazyloaded" alt="mercadopago" />
                        </li>
                        <li>
                            <img src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/pagofacil@2x.png" data-src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/pagofacil@2x.png" className="icon-logo lazyloaded" alt="pagofacil" />
                        </li>
                        <li>
                            <img src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/rapipago@2x.png" data-src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/rapipago@2x.png" className="icon-logo lazyloaded" alt="rapipago" />
                        </li>
                        <li>
                            <img src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/ar/tarjeta-naranja@2x.png" data-src="//d26lpennugtm8s.cloudfront.net/assets/common/img/logos/payment/new_logos_payment/ar/tarjeta-naranja@2x.png" className="icon-logo ls-is-cached lazyloaded" alt="ar_tarjeta-naranja" />
                        </li>
                    </ul>
                </div>
            </li>
            <li>
                <div>
                    <p>Contactos:</p>
                    <ul className='ulContacto'>
                        <p>uliisesrodriguez809@gmail.com</p>
                        <p>0351-555555</p>
                    </ul>
                </div>
            </li>
        </ul>
    </footer>
}
